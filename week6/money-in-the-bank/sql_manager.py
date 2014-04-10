import requests
import sqlite3
from hashlib import sha1
from Client import Client
import datetime 

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

__MAX_ATTEMPTS = 5

def create_clients_table():
    create_query = '''create table if not exists
        clients(id integer primary key,
                username text,
                email text,
                password text,
                balance real default 0,
                message text,
                attempts int default 0,
                time_to_wait int default 0)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = '''update clients set message = ?
            where id = ?'''
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    if _weak_password(logged_user.get_username(), new_pass):
        return False

    update_sql = '''update clients set password = ?
            where id = ?'''

    hashed_password = sha1(new_pass.encode('utf-8')).digest()
    cursor.execute(update_sql, (hashed_password, logged_user.get_id()))
    conn.commit()
    
    return True

def send_reset_key(email):
    import smtplib
    sender = 'from@moneyinthebank.org'
    key = sha1(email.encode('utf-8')).digest()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("dtaskoff@abv.bg", "dtaskoff@abv")
    server.sendmail(sender, email, key)
    server.close()

def reset_password(username, key):
    email = get_email(username)
    if key != sha1(email.encode('utf-8')).digest():
        return False

    update_sql = '''update clients set password = ?
            where id = ?'''

    hashed_password = sha1("aaAA11**".encode('utf-8')).digest()
    cursor.execute(update_sql, (hashed_password, logged_user.get_id()))
    conn.commit()

    return True

def get_email(username):
    select_email = '''select email from clients
        where username = ?'''
    email = cursor.execute(select_email, (username, )).fetchone()
    return email[0]

def _has_digit(password):
    digits = [char for char in password if char.isdigit()]
    return len(digits) > 0

def _has_lower(password):
    lowers = [char for char in password if char.islower()]
    return len(lowers) > 0

def _has_upper(password):
    uppers = [char for char in password if char.isupper()]
    return len(uppers) > 0

def _special(char):
    return not char.isupper() and not char.islower()\
        and not char.isdigit() and not char.isalpha()

def _has_special(password):
    specials = [char for char in password if _special(char)]
    return len(specials) > 0

def _is_long_enough(password):
    return len(password) >= 8

def _username_in_password(username, password):
    return username in password

def predicates():
    preds = [_has_special, _has_upper, _has_lower,
    _has_digit, _is_long_enough]
    return preds

def _weak_password(username, password):
    for pred in predicates():
        if not pred(password):
            return True

    return _username_in_password(username, password)

def register(username, email, password):
    if _weak_password(username, password):
        return False

    hash_password = sha1(password.encode('utf-8')).digest()

    insert_sql = '''insert into clients(username, email, password)
            values (?, ?, ?) '''
    cursor.execute(insert_sql, (username, email, hash_password))
    conn.commit()

    return True

def _user_exists(username):
    select_user = '''select id from clients where username = ?'''
    users = cursor.execute(select_user, (username, )).fetchone()
    return users != None

def _attempts(username):
    select_attempts = '''select attempts from clients
        where username = ?'''
    attempts = cursor.execute(select_attempts, (username,)).fetchone()
    return attempts[0]

def _reset_attempts(username):
    update_attempts = '''update clients set attempts = 0
        where username = ?'''
    cursor.execute(update_attempts, (username, ))
    conn.commit()

def _increment_attempts(username):
    attempts = _attempts(username)
    update_attempts = '''update clients set attempts = ?
        where username = ?'''
    cursor.execute(update_attempts, (attempts + 1, username))
    conn.commit()

def _timestamp(username):
    select_timestamp = '''select time_to_wait from clients
        where username = ?'''
    old_timestamp = cursor.execute(select_timestamp, (username, )).fetcone()
    old_timestamp = old_timestamp[0]

    if old_timestamp == 0:
        update_timestamp = '''update clients
            set time_to_wait = 5 where username = ?'''
        cursor.execute(update_timestamp, (username, ))
        conn.commit()
    else:
        pass

def login(username, password):
    if not _user_exists(username) or _attempts(username) > __MAX_ATTEMPTS:
        return False

    select_query = '''select id, username, email, balance, message
            from clients
            where username = ? and password = ?
            limit 1'''
    hashed_password = sha1(password.encode('utf-8')).digest()
    cursor.execute(select_query, (username, hashed_password))
    user = cursor.fetchone()

    if user:
        _reset_attempts(username)
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        _increment_attempts(username)
        return False

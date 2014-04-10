import requests
import sqlite3
from hashlib import sha1
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = '''update clients set message = ?
            WHERE id = ?'''
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

def register(username, password):
    if _weak_password(username, password):
        return False

    hash_password = sha1(password.encode('utf-8')).digest()

    insert_sql = '''insert into clients(username, password)
            values (?, ?) '''
    cursor.execute(insert_sql, (username, hash_password))
    conn.commit()

    return True


def login(username, password):
    select_query = '''select id, username, balance, message
            from clients
            where username = ? and password = ?
            limit 1'''
    hashed_password = sha1(password.encode('utf-8')).digest()
    cursor.execute(select_query, (username, hashed_password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False

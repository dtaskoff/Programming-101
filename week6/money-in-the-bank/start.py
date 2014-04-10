import sql_manager
from getpass import getpass


def main_menu():
    print('\n'.join(["Welcome to our bank service. You are not logged in.",
        "Please register or login"]))
    
    while True:
        command = input("$$$>")
        
        if command == 'register':
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = getpass("Enter your password: ")

            while sql_manager.register(username, email, password) == False:
                print(' '.join(["Password should contain an upper and",
                        "a lowercase letter, a digit and a symbol"]))
                password = getpass("Enter your password: ")
            
            print("Registration Successfull")

        elif command == "send-reset-password":
            username = input("Enter your username: ")
            email = sql_manager.get_email(username)
            sql_manager.send_reset_key(email)

        elif command == 'reset-password':
            username = input("Enter your username: ")
            key = input("Enter key: ")
            if not reset_password(username, key):
                print("Wrong key entered!")
            else:
                print('\n'.join(["Password set to aaAA11**",
                    "Please change your password now!"]))

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print('\n'.join(["Login failed",
                    "Maybe you'd entered wrong password more than 5 times?",
                    "If so, you've been blocked for 5 minutes.."]))
        
        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")

def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass("Enter your new password: ")
            while sql_manager.change_pass(new_pass, logged_user) == False:
                print(' '.join("Password should contain an upper and",
                        "a lowercase letter, a digit and a symbol"))
                new_pass = getpass("Enter your new password: ")

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)
        
        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()

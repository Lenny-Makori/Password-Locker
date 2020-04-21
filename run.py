#!/usr/bin/env python3.6
import pyperclip
from credentials import Credentials
from user import User

def user_login(first_name, last_name, login_password):
    user = User(first_name, last_name, login_password)
    return user

def save_user_login(user):
    user.save_user()

def user_authentication(fuser):
    return User.find_password_for(fuser)


def add_existing_account(password_for, username, password):
    existing_account = Credentials(password_for, username, password)
    return existing_account

def add_new_account(password_for, username, password):
    new_account = Credentials(password_for, username, password)
    return new_account

def save_account(account):
    account.save_account()

def generate_password_for(username):
    Credentials.generate_password_for(username)
    pyperclip.paste()

def view_accounts():
    return Credentials.display_accounts()

def delete_account(password_for):
    Credentials.delete_account(password_for)


def main():
    print("Hello welcome to your password locker. Do you have an account? (reply with 'yes' or 'no')")
    response = input().lower()
    print('\n')

    while True:

        if response == 'no':
            print("Create your account here:")
            print("First Name:")
            fname = input()
            print("Last Name:")
            lname = input()
            print("Enter new password:")
            logpassword = input()
            print("Confirm password:")
            logpassword2 = input()

            if logpassword == logpassword2:
                save_user_login(user_login(fname, lname, logpassword))
                print(f"{fname}, you have successfully created your Password Locker account has been created! Look around and see what you can do to you account!")

            else:
                print("Incorrect password confirmation. Kindly enter your password again")
                print("Enter new password:")
                logpassword = input()
                print("Confirm password:")
                logpassword2 = input()
                if logpassword == logpassword2:
                    save_user_login(user_login(fname, lname, logpassword))
                    print('\n')
                    print(f"{fname}, you have successfully created your Password Locker account has been created! Look around and see what you can do to you account!")
                    print('\n')

            while True:
                print('\n')
                print("="*50)
                print("What would you like to do? Reply with the following short codes. ea - add an existing account, na - add a new account, da - display all accounts, dl - delete an account")
                short_code = input().lower()

                if short_code == "ea":
                    print("please fill in the details below.")
                    print("Account name:")
                    account_name = input().lower()
                    print("Username:")
                    user_name = input()
                    print("Enter password:")
                    user_password = input()

                    save_account(add_existing_account(account_name, user_name, user_password))
                    print('\n')
                    print(f"Your {account_name} account has been added.")

                elif short_code == "na":
                    print("please fill in the details below.")
                    print("Account name:")
                    account_name = input().lower()
                    print("Username:")
                    user_name = input()
                    print("Enter password:")
                    user_password = input()
                    print("Confirm password:")
                    user_password2 = input()

                    if user_password == user_password2:
                        save_account(add_existing_account(account_name, user_name, user_password))
                        print('\n')
                        print(f"Your {account_name} account has been added.")

                    else:
                        print("Invalid password confirmation. Kindly enter your password again")
                        print("Enter password:")
                        user_password = input()
                        print("Confirm password:")
                        user_password2 = input()

                        if user_password == user_password2:
                            save_account(add_existing_account(account_name, user_name, user_password))
                            print('\n')
                            print(f"Your {account_name} account has been added.")

                elif short_code == "da":
                    if view_accounts():
                        print("Here is a list of all your contacts")
                        print ('\n')

                        for account in view_accounts():
                            print(f" ACCOUNT:=> {account.password_for} || Username: => {account.username} || Password: => {account.password}")
                            print('-'*10)

                    else:
                        print ('\n')
                        print("You don't seem to have any accounts yet")
                        print('\n')

                elif short_code == "dl":
                    print("Enter the name of the account that you want to delete:")
                    account_name = input().lower()
                    delete_account(account_name)
                    print('\n')
                    print(f"Your {account_name} account has been deleted")

                elif short_code == "ex":
                    print('\n')
                    print(f"******Bye {fname}******")
                    print('\n')
                    break

                else:
                    print("I really didn't get that, kindly use the short codes")


        elif response == "yes":
            print("Enter your Name here:")
            print("First Name:")
            fname = input()

            print("Enter password:")
            logpassword = input()

            if logpassword == user_authentication(fname):
                print(f" Welcome {fname}. You have successfully logged in.")
                print('\n')
                print("="*10)
            

            else:
                print("Invalid user name or password")
                print('\n')
        

        else:
            print(" I didn't get that, kindly reply with 'yes' or 'no'")
            break

if __name__ == "__main__":
    main()



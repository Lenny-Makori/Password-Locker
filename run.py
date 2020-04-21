import pyperclip
from credentials import Credentials
from user import User

def user_login(self, first_name, last_name, login_password):
    self.user = User(first_name, last_name, login_password)

def save_user_login(user):
    user.save_user()


def add_existing_account(self, password_for, username, password):
    self.existing_account = Credentials(password_for, username, password)

def add_new_account(self, password_for, username, password):
    self.new_account = Credentials(password_for, username, password)

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

    if response == 'yes':
        print("Enter your Name here:")
        print("First Name:")
        lname = input()
        print("Enter password:")
        logpassword = input()
        



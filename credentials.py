import pyperclip
class Credentials:

    accounts_list = []

    def save_account(self):
        Credentials.accounts_list.append(self)

    @classmethod
    def generate_password_for(cls, username):
        for account in cls.accounts_list:
            if account.username == username:
                pyperclip.copy(account.password)

    @classmethod
    def  display_accounts(cls):
        return cls.accounts_list

    @classmethod
    def delete_account(cls, password_for):
        for account in cls.accounts_list:
            if account.password_for == password_for:
                cls.accounts_list.remove(account)


    def __init__(self, password_for, username, password):

        self.password_for = password_for
        self.username = username
        self.password = password
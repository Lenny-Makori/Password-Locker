import pyperclip
class Credentials:
    """
    Class that generates new instances of account credentials
    """

    accounts_list = []

    def save_account(self):
        """
        save_account method to save new account to accounts_list
        """
        Credentials.accounts_list.append(self)

    @classmethod
    def generate_password_for(cls, username):
        """
        Method that takes in a username and returns the account's password
        """
        for account in cls.accounts_list:
            if account.username == username:
                pyperclip.copy(account.password)

    @classmethod
    def  display_accounts(cls):
        """
        method that returns the accounts list
        """
        return cls.accounts_list

    @classmethod
    def delete_account(cls, password_for):
        """
        method that deletes an account from the accounts list
        """
        for account in cls.accounts_list:
            if account.password_for == password_for:
                cls.accounts_list.remove(account)


    def __init__(self, password_for, username, password):

        self.password_for = password_for
        self.username = username
        self.password = password
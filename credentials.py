class Credentials:

    accounts_list = []

    def save_account(self):
        Credentials.accounts_list.append(self)


    def __init__(self, password_for, username, password):

        self.password_for = password_for
        self.username = username
        self.password = password
class User:

    users_list = []

    def save_user(self):
        """
        method to save user profile credentials
        """
        User.users_list.append(self)

    @classmethod
    def find_password_for(cls, fname):
        """
        method to return password for a registered user
        """
        for user in cls.users_list:
            if user.user_first_name == fname:
                return user.login_password

    def __init__(self, user_first_name, user_last_name, login_password):

        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.login_password = login_password
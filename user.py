class User:

    users_list = []

    def __init__(self, user_first_name, user_last_name, login_password):

        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.login_password = login_password
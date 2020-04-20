from user import User
from credentials import Credentials
import unittest


class TestAccount(unittest.TestCase):

    def setUp(self):
        '''
        setup to run before all test cases
        '''

        self.new_user = User("Lenny", "Makori", "moringastudent001")

    def tearDown(self):
        Credentials.accounts_list = []

    def test_init(self):
        '''
        test case to check if the user is logged in properly
        '''
        self.assertEqual(self.new_user.user_first_name, "Lenny")
        self.assertEqual(self.new_user.user_last_name, "Makori")
        self.assertEqual(self.new_user.login_password, "moringastudent001")

# if __name__ == "__main__":
#     unittest.main()


    def test_add_existing_account(self):
        self.new_existing_account = Credentials("twitter", "lennymakori1", "makorimakori28")

        self.assertEqual(self.new_existing_account.password_for, "twitter")
        self.assertEqual(self.new_existing_account.username, "lennymakori1")
        self.assertEqual(self.new_existing_account.password, "makorimakori28")

# if __name__ == "__main__":
#     unittest.main()


    def test_add_new_account(self):
        self.new_account = Credentials("instagram", "makorilenny1", "28lennylenny")

        self.assertEqual(self.new_account.password_for, "instagram")
        self.assertEqual(self.new_account.username, "makorilenny1")
        self.assertEqual(self.new_account.password, "28lennylenny")

# if __name__ == "__main__":
#     unittest.main()


    def test_save_account(self):
        self.new_existing_account = Credentials("twitter", "lennymakori1", "makorimakori28")
        self.new_existing_account.save_account()

        self.assertEqual(len(Credentials.accounts_list), 1)

# if __name__ == "__main__":
#     unittest.main()


    def test_multiple_accounts(self):
        self.new_existing_account = Credentials("twitter", "lennymakori1", "makorimakori28")
        self.new_account = Credentials("instagram", "makorilenny1", "28lennylenny")
        self.new_existing_account.save_account()
        self.new_account.save_account()

        self.assertEqual(len(Credentials.accounts_list), 2)

# if __name__ == "__main__":
#     unittest.main()

    

if __name__ == "__main__":
    unittest.main()

        

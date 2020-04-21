from user import User
from credentials import Credentials
import unittest
import pyperclip


class TestAccount(unittest.TestCase):

    def setUp(self):
        """
        setup to run before all test cases
        """

        self.new_user = User("Lenny", "Makori", "moringastudent001")

    def tearDown(self):
        Credentials.accounts_list = []

    def test_init(self):
        """
        test case to check if the user is logged in properly
        """
        self.assertEqual(self.new_user.user_first_name, "Lenny")
        self.assertEqual(self.new_user.user_last_name, "Makori")
        self.assertEqual(self.new_user.login_password, "moringastudent001")

# if __name__ == "__main__":
#     unittest.main()

    def test_save_user(self):
        """
        test case to test if a user profile can be saved
        """
        self.new_user.save_user()

        self.assertEqual(len(User.users_list), 1)

    def test_user_password_by_firstname(self):
        """
        test case to test authentication of user's password and username
        """
        found_password = User.find_password_for("Lenny")

        self.assertEqual(found_password, self.new_user.login_password)


    def test_add_existing_account(self):
        """
        test case to test adding an existing account's credentials
        """
        self.new_existing_account = Credentials("twitter", "lennymakori1", "makorimakori28")

        self.assertEqual(self.new_existing_account.password_for, "twitter")
        self.assertEqual(self.new_existing_account.username, "lennymakori1")
        self.assertEqual(self.new_existing_account.password, "makorimakori28")

# if __name__ == "__main__":
#     unittest.main()


    def test_add_new_account(self):
        """
        test case to test adding a new account's credentials
        """
        self.new_account = Credentials("instagram", "makorilenny1", "28lennylenny")

        self.assertEqual(self.new_account.password_for, "instagram")
        self.assertEqual(self.new_account.username, "makorilenny1")
        self.assertEqual(self.new_account.password, "28lennylenny")

# if __name__ == "__main__":
#     unittest.main()


    def test_save_account(self):
        """
        test case to test saving an account's credentials
        """
        self.new_existing_account = Credentials("twitter", "lennymakori1", "makorimakori28")
        self.new_existing_account.save_account()

        self.assertEqual(len(Credentials.accounts_list), 1)

# if __name__ == "__main__":
#     unittest.main()


    def test_multiple_accounts(self):
        """
        test case to test saving multiple accounts' credentials
        """
        self.new_existing_account = Credentials("twitter", "lennymakori1", "makorimakori28")
        self.new_account = Credentials("instagram", "makorilenny1", "28lennylenny")
        self.new_existing_account.save_account()
        self.new_account.save_account()

        self.assertEqual(len(Credentials.accounts_list), 2)

# if __name__ == "__main__":
#     unittest.main()

    def test_generate_password(self):
        """
        test case to test generating a password for new account
        """
        self.new_existing_account = Credentials("twitter", "lennymakori1", "makorimakori28")
        self.new_account = Credentials("instagram", "makorilenny1", "28lennylenny")
        self.new_existing_account.save_account()
        self.new_account.save_account()

        Credentials.generate_password_for("makorilenny1")

        self.assertEqual(self.new_account.password, pyperclip.paste())

# if __name__ == "__main__":
#     unittest.main()

    def test_view_accounts(self):
        """
        test case to test displaying added accounts credentials
        """
        self.new_existing_account = Credentials("twitter", "lennymakori1", "makorimakori28")
        self.new_account = Credentials("instagram", "makorilenny1", "28lennylenny")
        self.new_existing_account.save_account()
        self.new_account.save_account()
        
        self.assertEqual(Credentials.display_accounts(), Credentials.accounts_list)

# if __name__ == "__main__":
#     unittest.main()

    def test_delete_account(self):
        """
        test case to test deleting an account's credentials
        """
        self.new_existing_account = Credentials("twitter", "lennymakori1", "makorimakori28")
        self.new_account = Credentials("instagram", "makorilenny1", "28lennylenny")
        self.new_existing_account.save_account()
        self.new_account.save_account()

        Credentials.delete_account("twitter")

        self.assertEqual(len(Credentials.accounts_list), 1)

if __name__ == "__main__":
    unittest.main()
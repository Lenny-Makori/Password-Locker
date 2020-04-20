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


    
if __name__ == "__main__":
    unittest.main()

        

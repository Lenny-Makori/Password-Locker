from user import User
from credentials import Credentials
import unittest


class TestAccount(unittest.TestCase):

    def setUp(self):
        '''
        setup to run before all test cases
        '''

        self.new_user = User("Lenny", "Makori", "moringastudent001")

    
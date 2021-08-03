import unittest #Importimg the unittest module
from password import User #Importing the User class
from password import Credentials #Importing the Credentials class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that aids in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run each test case.
        '''
        self.new_user = User("Monsqih", "monsq!H!997") #Creates user object
        self.new_credentials = Credentials("Twitter", "Monsq!h!997") #Creates credentials object

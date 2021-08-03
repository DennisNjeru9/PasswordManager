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


    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run t avoid repitition of input. 
        '''

        User.user_list = []


    def test_init (self):
        '''
        test init test case to test the proper initialization of user and credentials objects.
        '''

        self.assertEqual(self.new_user.username,"Monsqih")
        self.assertEqual(self.new_user.password,"monsq!H!997")

# if __name__ == '__main__':
#     unittest.main()


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that aids in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run each test case.
        '''

        self.new_credentials = Credentials("Twitter", "thePhi", "Monsq!h!997") #Creates credentials object

    
    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run t avoid repitition of input. 
        '''
        Credentials.credentials_list = []


    def test_init (self):
        '''
        test init test case to test the proper initialization of user and credentials objects.
        '''

        self.assertEqual(self.new_credentials.account_name,"Twitter")
        self.assertEqual(self.new_credentials.account_username,"thePhi")
        self.assertEqual(self.new_credentials.account_password,"Monsq!h!997")


    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into credentials_list object.
        '''

        self.new_credentials.save_credentials() #saving new credentials
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_save_multiple_credentials(self):
        '''
        test_save_credentials test case to establish if multiple credentials objects can be saved into the credentials_list object.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","Kata-naah", "n@4HK@t4")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)


if __name__ == '__main__':
    unittest.main()


class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] #Empty user list

    def __init__(self, username, password):

        '''
        __init__ method that enables the definition of properties for the user objects.

        Args:
            username: User's name for login.
            password: User's password to authenticate login.
        '''

        self.username = username
        self.password = password

    pass


class Credentials:
    '''
    Class that generates new instances of credentials.
    '''

    def __init__(self, account_name, account_username, account_password):
        '''
        Args:
            account_name: The name of the account.
            account_password: The password for the corresponding account.
        '''

        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    pass
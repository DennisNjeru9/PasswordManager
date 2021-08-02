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
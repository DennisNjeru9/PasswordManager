#!/usr/bin/env python3.8
from password import User
from password import Credentials

#Create an account
def create_user(username,password):
    '''
    Function to create a new user account.
    '''

    new_user = User(username,password)
    return new_user


#Create a new credential
def create_credentials(aname,ausername,apassword):
    '''
    Function to create a new credential.
    '''

    new_credentials = Credentials(aname,ausername,apassword)
    return new_credentials


#Save credentials
def save_credentials(credentials):
    '''
    Function to save credentials.
    '''

    credentials.save_credentials()




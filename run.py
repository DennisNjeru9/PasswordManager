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


#Delete credentials
def delete_credentials(credentials):
    '''
    Function to delete credentials.
    '''

    credentials.delete_credentials()


#Finding credentials
def find_credential(aname):
    '''
    Function that helps users to find a credential by name and return the credentials.
    '''

    return Credentials.find_credentials_by_account_name(aname)


#Checking if credentials exist
def check_existing_credentials(aname):
    '''
    Function that allows users to check if credentials exist with the account name and return a Boolean.
    '''
    return Credentials.credentials_exist(aname)


#Displaying all credentials
def display_credentials():
    '''
    Function that returns all the saved credentials.
    '''
    return Credentials.display_credentials()



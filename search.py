# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:31:12 2024

@author: Riley Outlaw, Ethan Stewart
"""

import pickle
from pythonHashing import hash_data

pickled_file = "hashedValues.pkl"
debug_preHashed = True
empty_hashed = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

# A function to export debug_preHashed
def debug_preHashed():
    return debug_preHashed

# Reads in a credential file from pickle
def read_credentials_from_pickle(pickled_file):
    with open(pickled_file, "rb") as pickle_file:
        return pickle.load(pickle_file)

# Creates the credentials object
credentials = read_credentials_from_pickle(pickled_file)

# Returns a message response based on search results
def search(email, password):
    if email == empty_hashed:
        return "Please Submit an Email and Password"
    if not debug_preHashed:
        email = hash_data(email)
        password = hash_data(password)
    if not email in credentials:
        return "Your information was not found in the database!"
    if credentials[email] == password:
        return "Unfortunately, your information was found in the database."
    else:
        return "Your email is in the database, but your password is not."

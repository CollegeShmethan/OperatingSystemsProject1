# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:11:06 2024

@author: Riley Outlaw, Ethan Stewart
"""

import hashlib
import pickle

credential_files = ["credentials1.txt", "credentials2.txt"]
output_text = "hashedValues.txt"
output_pickle = "hashedValues.pkl"

sha256 = hashlib.sha256()
credentials = {}

# Hashes data
def hash_data(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))  
    return sha256.hexdigest()

# Reads in credential files and uses the credentials object to store them.
def read_and_insert(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                email, password = line.strip().split(":", 1)
                email_hash = hash_data(email)
                password_hash = hash_data(password)
                credentials[email_hash] = password_hash    
            except:
                continue

# Saves credentials to a file
def save_credentials_to_text(credentials, file_path):
    with open(file_path, "w") as file:
        for email, password in credentials.items():
            file.write(f"{email}:{password}\n")

# Saves credentials to a file
def save_credentials_to_pickle(credentials, file_path):
    with open(file_path, "wb") as pickle_file:
        pickle.dump(credentials, pickle_file)


def read_and_save_credentials():
    # Read data from file and insert into database
    for credential_file in credential_files:
        read_and_insert(credential_file)

    save_credentials_to_pickle(credentials, output_pickle)

#   Run only when needed
#   read_and_save_credentials()

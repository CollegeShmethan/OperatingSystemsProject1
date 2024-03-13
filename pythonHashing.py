# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:11:06 2024

@author: Riley Outlaw, Ethan Stewart
"""

import hashlib

sha256 = hashlib.sha256()
credentials = {}

def hash_data(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))  
    return sha256.hexdigest()

def read_and_insert(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                email, password = line.strip().split(":",1)
                email_hash = hash_data(email)
                password_hash = hash_data(password)
                credentials[email_hash] = password_hash    
            except:
                continue

def save_credentials(credentials, file_path):
    with open(file_path, "w") as file:
        for email, password in credentials.items():
            file.write(f"{email}:{password}\n")

# Read data from file and insert into database
read_and_insert("credentials1.txt")
read_and_insert("credentials2.txt")

file_path="hashedValues.txt"
save_credentials(credentials, file_path)

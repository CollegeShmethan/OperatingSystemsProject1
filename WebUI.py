# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:29:50 2024

@author: Riley Outlaw, Ethan Stewart
"""

from flask import Flask
webUI = Flask(__name__)   # Flask constructor

@webUI.route('/')
def index():
    return "Blah"

if __name__ == '__main__':
    webUI.run()

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:29:50 2024

@author: Riley Outlaw, Ethan Stewart
"""

from flask import Flask, request, render_template
from search import search
webUI = Flask(__name__)   # Flask constructor

# Known issue - Last message shows up on the reloaded page.

#   The way this is done is absolutely not safe. 
#   All requests made are online and can be accessed maliciously. 
#   The better way to do this would be to hash 
#   the username and password immediately upon form submission.

@webUI.route('/', methods=['GET', 'POST'])
def index():
    email = None
    password = None
    foundMessage = "Awaiting Submit"
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        foundMessage = search(email, password)

    return render_template("index.html", fndMessage = foundMessage)

if __name__ == '__main__':
    webUI.run()

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:29:50 2024

@author: Riley Outlaw, Ethan Stewart
"""

from flask import Flask, request, render_template
from search import search, debug_preHashed
webUI = Flask(__name__)   # Flask constructor

if(debug_preHashed()):
    debug_preH = 1
else:
    debug_preH = 0

#   Known issue - Last message shows up on the reloaded page.
#   This is because the form is maintaining the information submitted,
#   and comes from the browser, not the code.

#   The way this is done in python without debug_preHashed is not secure. 
#   A post request is made and can be accessed maliciously. 
#   The better way to do this would be to hash 
#   the username and password immediately upon form submission.

@webUI.route('/', methods=['GET', 'POST'])
def index():
    email = None
    password = None
    foundMessage = "Please Submit an Email and Password"
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        foundMessage = search(email, password)

    return render_template("index.html", fndMessage=foundMessage, preHashed = debug_preH)

if __name__ == '__main__':
    webUI.run()

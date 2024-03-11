# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:29:50 2024

@author: Riley Outlaw, Ethan Stewart
"""

from flask import Flask, render_template
webUI = Flask(__name__)   # Flask constructor

@webUI.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    webUI.run()

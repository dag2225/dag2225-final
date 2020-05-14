# -*- coding: utf-8 -*-
"""
@author: Devin Golla
UNI: dag2225
Overview of Program: Utilizes Flask library to set up routes for navigation between pages
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/") 
# if you go to this home route, then it will show whatever you define this function to you
def index():
    """
    Specifies action of home page route
    """
    return render_template("index.html")

@app.route("/assignments.html") 
def assignments():
    """
    Specifies action of assignment page route
    """
    return render_template("/assignments.html")

@app.route("/classes.html") 
def classes():
    """
    Specifies action of classes page route
    """
    return render_template("/classes.html")

#start the server
if __name__ == "__main__":
    app.run()
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: Devin Golla
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/") 
# if you go to this home route, then it will show whatever you define this function to you
def hello():
    return render_template("index.html")

@app.route("/assignments.html") 
def hello1():
    return render_template("/assignments.html")

@app.route("/classes.html") 
def hello2():
    return render_template("/classes.html")

#start the server
if __name__ == "__main__":
    app.run()
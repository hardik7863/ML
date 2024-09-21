### Flask basic skelton
from flask import Flask
"""
It creates an instance of the flask class,
which will be your WSGI (Web Server Gateway Interface)application.

"""

###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course.This should be an amazing course"

@app.route("/index")
def index():
    return "welcome to index page"
# below is the entry point of any app.py file
if __name__=="__main__":
    app.run(debug=True)
    # here debug act as nodemon not nedd to restart the server again
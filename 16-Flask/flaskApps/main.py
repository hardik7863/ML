## Integrating HTML and FLASK Web App

from flask import Flask,render_template
"""
It creates an instance of the flask class,
which will be your WSGI (Web Server Gateway Interface)application.

"""

###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to this best Flask course</h1></html>"

#Since we cannot write big html code here we will use render_template to 
# use html file completely 

@app.route("/index")
def index():
    return render_template('index.html')
# we will not create direct html file in the same folder 
# instead we will create a folder templates and create html file inside it
# this error is due to jinja 



@app.route("/about")
def about():
    return render_template('about.html')




# below is the entry point of any app.py file
if __name__=="__main__":
    app.run(debug=True)
    # here debug act as nodemon not nedd to restart the server again
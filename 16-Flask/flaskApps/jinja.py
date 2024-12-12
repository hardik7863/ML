### Building URL dynamically
## variable Rule
## Jinja 2 Template Engine

### JInja 2 Template Engine
'''
{{ }} expressions to print output in html
{%...%} conditions,for loops
{#....#} this is for comments
'''



from flask import Flask,render_template,request,redirect,url_for
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

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')
# we will not create direct html file in the same folder 
# instead we will create a folder templates and create html file inside it
# this error is due to jinja 



@app.route("/about")
def about():
    return render_template('about.html')



# @app.route("/submit",methods=['GET','POST'])
# def submit():
#     if request.method=="POST":
#         name=request.form['name']
#         # id=['name']
#         return f'Hello {name}'
#     return render_template('form.html')

## Variable Rule:- only int or only float value can be passed
# @app.route('/success/<int:score>')
# def success(score):
#     return "The marks you got is" + str(score)
# typecaste to string 

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}
    return render_template('result1.html',results=exp)

#if condition
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form["science"])
        maths=float(request.form["maths"])
        c=float(request.form['c'])
        data_science=float(request.form["datascience"])
        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))

# below is the entry point of any app.py file
if __name__=="__main__":
    app.run(debug=True)
    # here debug act as nodemon not nedd to restart the server again
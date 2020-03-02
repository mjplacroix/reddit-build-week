"""test page for Flask and Heroku"""


from flask import Flask, render_template

# make the application
app = Flask(__name__)

# make the route
@app.route("/")

#def a function
def hello():
    return "Testing text for Reddit and Heroku..."

# # make second route
# @app.route("/about")

# # func for about
# def preds():
#     return render_template('about.html')
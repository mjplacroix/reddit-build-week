"""test page for Flask and Heroku"""
from flask import Flask, render_template

# make the application
#APP = Flask(__name__)

def create_app():
    app = Flask(__name__)
    
    # make the route
    @app.route("/")
        return "Testing text for Reddit and Heroku..."





# # make second route
# @app.route("/about")

# # func for about
# def preds():
#     return render_template('about.html')
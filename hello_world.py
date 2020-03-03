"""test page for Flask and Heroku"""
from flask import Flask, render_template


app = Flask(__name__)
# make the application
#APP = Flask(__name__)
    # app = Flask(__name__)
    # make the route
@app.route("/")
def create_app():
    return "Testing text for Reddit and Heroku..."





# # make second route
# @app.route("/about")

# # func for about
# def preds():
#     return render_template('about.html')
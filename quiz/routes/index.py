from flask import render_template
from app import app

@app.route("/")
def home():
    '''
    the home page of the application
    '''
    return render_template('home.html')


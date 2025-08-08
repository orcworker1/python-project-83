from flask import render_template

from __init__ import app



@app.route('/')
def index():
    return "Welcome to Page Analyzer!"
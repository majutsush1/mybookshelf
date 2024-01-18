from flask import current_app as app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/<page>')
def route(page):
    return render_template(page)
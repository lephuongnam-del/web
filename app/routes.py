from app import app
from flask import render_template, session, request, redirect, url_for, flash, make_response, session

@app.route('/')
def index():
    return render_template('index.html')

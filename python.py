#code to follow
from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3 as sql

app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/searchresults', methods=['POST', 'GET'])
def search_results():
    return render_template('searchresults.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

if __name__=='__main__':
    app.run(debug=True)
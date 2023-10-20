#code to follow
from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3 as sql

app= Flask(__name__)
@app.route('/')
def home():
  return render_template('homesqlProject.html')

@app.route('/enterdetails')
def enterdetails():
  return render_template('enterdetails.html')

@app.route('/flightbooked')
def flightbooked():
  return render_template('flightbooked.html')

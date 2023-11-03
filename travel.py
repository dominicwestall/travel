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

@app.route('/usermustlogin', methods=['POST', 'GET'])
def usermustlogin():
    return render_template('signin.html')

@app.route('/reviewsubmission', methods=['POST', 'GET'])
def reviewsubmission():
    return render_template('reviewsthankyou.html')

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

@app.route('/usersignin', methods=['POST','GET'])
def user_signin():
    # this is the login functionality
    # current design of the login system
    # if authentication is successful, the user is redirected to the home page
    # if not, the user gets an error message and can try again.
    if request.method == "POST":
        msg = None
        emailaddressofuser = request.form['email']
        passwordofuser = request.form['password']
        con = sql.connect("travellogin.db")
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute("select * from Users where Email=? and Password=?", (emailaddressofuser, passwordofuser))
        rows=cur.fetchone()
        if rows:
            con.close()
            return render_template('booking made.html')
        else:
            con.close()
            msg = "Wrong email address and/or password!"
            return render_template('signin.html', msg=msg)

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/registertheuser', methods=['POST','GET'])
def registertheuser():
    # code to insert a record into the travel login database.
    if request.method == 'POST':
        emailaddressofuser = request.form['email']
        passwordofuser = request.form['password']
        confirmpasswordofuser = request.form['confirmpassword']
        if not emailaddressofuser or passwordofuser:
            # if the password fields do not match, return an error
            if confirmpasswordofuser != passwordofuser:
                msg = "Passwords do not match"
                return render_template('registration.html', msg=msg)
            else:
                with sql.connect("travellogin.db") as con:
                    cur = con.cursor()
                    cur.execute("insert into Users(Email, Password) values (?,?)", (emailaddressofuser, passwordofuser))
                    con.commit()
                    msg = "New user successfully added"
                    
        else:
            msg = "New user: error in insert operation"
            con.rollback()
            return render_template('registration.html', msg=msg)
    
    # send the user back to the home page once successful.
        return render_template('index.html', msg=msg)

if __name__=='__main__':
    app.run(debug=True)

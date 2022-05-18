from flask import render_template, redirect, url_for, session, request
from app import db
from . import main
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash



# user signup route function
@main.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['s-email']
        name = request.form['s-name']
        password = request.form['s-password']
        if email and name and password:
            new_user = User(name, email, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            session['username'] = name
            session['password'] = password
            return redirect(url_for('main.dashboard', user=new_user), code=307)
        else:
            # return a flash message for an unsuccessful signup
            return redirect(url_for('main.home'))
    else:
        return redirect(url_for('main.home'))



# user login route function
@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['l-email']
        password = request.form['l-password']
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                session['username'] = user.name
                session['password'] = user.password
                return redirect(url_for('main.dashboard', username=user.name), code=307)
            else:
                # include a flash message here to indicate wrong password
                return redirect(url_for('main.home'))
        else:
            return redirect(url_for('main.home'))
    else:
        return redirect(url_for('main.home'))
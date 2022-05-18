from flask import render_template, redirect, url_for, request, session
from . import main
from app.models import User


@main.route('/')
def home():
    if session:
        return redirect(url_for('main.dashboard', username=session['username']))
    else:
        return render_template('index.html')


@main.route('/user/<username>', methods=['POST', 'GET'])
def dashboard(username):
    user = User.query.filter_by(name=username).first()
    return render_template('user.html', user=user)
    

@main.route('/logout')
def sign_out():
    session.clear()
    return redirect(url_for('main.home'))




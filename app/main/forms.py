from flask import render_template, redirect, url_for, session, request
from app import db
from . import main
from app.models import Feedback, Question, ShoutOut, User
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
            session['email'] = email
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
                session['email'] = email
                session['password'] = user.password
                return redirect(url_for('main.dashboard', username=user.name), code=307)
            else:
                # include a flash message here to indicate wrong password
                return redirect(url_for('main.home'))
        else:
            return redirect(url_for('main.home'))
    else:
        return redirect(url_for('main.home'))



# user sharing route function
@main.route('/share', methods=['POST', 'GET'])
def share():
    if request.method == 'POST':
        present_user = User.query.filter_by(email=session['email']).first()
        if present_user:
            category = request.form['category']
            topic = request.form['about']
            content = request.form['share-form']
            if category.lower() == 'questions':
                new_question = Question(category=category, topic=topic, content=content, user_id=present_user.id)
                db.session.add(new_question)
                db.session.commit()
            elif category.lower() == 'feedback':
                new_feedback = Feedback(category=category, topic=topic, content=content, user_id=present_user.id)
                db.session.add(new_feedback)
                db.session.commit()
            else:
                new_shout_out = ShoutOut(category=category, topic=topic, content=content, user_id=present_user.id)
                db.session.add(new_shout_out)
                db.session.commit()
            return redirect(url_for('main.dashboard', username=present_user.name))
        else:
            return redirect(url_for('main.home'))
    else:
        return redirect(url_for('main.home'))



# commenting functionality
@main.route('/comment/<thought_id>', methods=['POST', 'GET'])
def comment(thought_id):
    if request.method == 'POST':
        # user = User.query.filter_by(name=session.get('user')).first()
        # new_comment = Comment(comment = request.form['comment'], user_id=user.id, pitch_id=pitch_id)
        # db.session.add(new_comment)
        # db.session.commit()
        return redirect(url_for('user', username = session['user']), code=307)
    else:
        return redirect(url_for('user', username = session['user']), code=307)


from flask import redirect, url_for, session, request, flash
from app import db
from . import main
from app.models import Feedback, FeedbackComment, Question, QuestionComment, ShoutOut, ShoutOutComment, User
from werkzeug.security import generate_password_hash, check_password_hash
import re


# user signup route function
@main.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['s-email']
        name = request.form['s-name']
        password = request.form['s-password']
        check = User.query.filter_by(email=email).first()
        if check:
            flash("This user already exists, login to your accout!", "warning")
            return redirect(url_for('main.home'))
        else:
            if email and name and password:
                regex = "@([a-z\S]+)"
                result = re.split(regex, email)
                if result[1] == "student.moringaschool.com":
                    new_user = User(name, email, generate_password_hash(password))
                    db.session.add(new_user)
                    db.session.commit()
                    session['username'] = name
                    session['email'] = email
                    session['password'] = password
                    return redirect(url_for('main.dashboard', username=new_user.name), code=307)
                elif result[1] == "moringaschool.com":
                    new_user = User(name, email, generate_password_hash(password))
                    db.session.add(new_user)
                    db.session.commit()
                    session['username'] = name
                    session['email'] = email
                    session['password'] = password
                    return redirect(url_for('main.staff_dashboard', username=new_user.name), code=307)
                else:
                    # return a flash message for a wrong email used
                    flash("Please Signup using a valid Moringa School email!", "warning")
                    return redirect(url_for('main.home'))
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
                regex = "@([a-z\S]+)"
                result = re.split(regex, email)
                if result[1] == "student.moringaschool.com":
                    return redirect(url_for('main.dashboard', username=user.name), code=307)
                elif result[1] == "moringaschool.com":
                    return redirect(url_for('main.staff_dashboard', username=user.name), code=307)
                else:
                    flash("Please use a valid Moringa School email!", "warning")
                    return redirect(url_for('main.home'))
            else:
                # include a flash message here to indicate wrong password
                flash("Please have entered the wrong password!", "warning")
                return redirect(url_for('main.home'))
        else:
            flash("User doesn't seem to exist. Make sure to check your spelling!", "warning")
            return redirect(url_for('main.home'))
    else:
        flash("You are not permitted to access this route using that method!", "warning")
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
@main.route('/feedback-comment/<feedback_id>', methods=['POST', 'GET'])
def feedback_comment(feedback_id):
    if request.method == 'POST':
        user = User.query.filter_by(email=session.get('email')).first()
        if request.form['comment']:
            new_comment = FeedbackComment(comment = request.form['comment'], feedback_user_id=user.id, feedback_id=feedback_id)
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('main.dashboard', username = user.name), code=307)
        else:
            return redirect(url_for('main.dashboard', username = user.name), code=307)
    else:
        return redirect(url_for('main.dashboard', username = user.name), code=307)


# commenting functionality
@main.route('/question-comment/<question_id>', methods=['POST', 'GET'])
def question_comment(question_id):
    if request.method == 'POST':
        user = User.query.filter_by(email=session.get('email')).first()
        if request.form['comment']:
            new_comment = QuestionComment(comment = request.form['comment'], question_user_id=user.id, question_id=question_id)
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('main.dashboard', username = user.name), code=307)
        else:
            return redirect(url_for('main.dashboard', username = user.name), code=307)
    else:
        return redirect(url_for('main.dashboard', username = user.name), code=307)


# commenting functionality
@main.route('/shoutout-comment/<shoutout_id>', methods=['POST', 'GET'])
def shoutout_comment(shoutout_id):
    if request.method == 'POST':
        user = User.query.filter_by(email=session.get('email')).first()
        if request.form['comment']:
            new_comment = ShoutOutComment(comment = request.form['comment'], shoutout_user_id=user.id, shoutout_id=shoutout_id)
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('main.dashboard', username = user.name), code=307)
        else:
            return redirect(url_for('main.dashboard', username = user.name), code=307)
    else:
        return redirect(url_for('main.dashboard', username = user.name), code=307)


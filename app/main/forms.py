"""
    Main Application Routes and Functionality

    This module contains various route functions for the main application. It handles user signup, login, and sharing functionality,
    along with commenting on different categories (feedback, questions, shoutouts).

    Functions:
        signup(): Handles the user signup process.
        login(): Handles the user login process.
        share(): Handles the user sharing functionality.
        feedback_comment(feedback_id): Handles commenting on feedback.
        question_comment(question_id): Handles commenting on questions.
        shoutout_comment(shoutout_id): Handles commenting on shoutouts.
"""

from flask import redirect, url_for, session, request, flash
from .. import db
from . import main
from ..models import Feedback, FeedbackComment, Question, QuestionComment, ShoutOut, ShoutOutComment, User
from werkzeug.security import generate_password_hash, check_password_hash
import re


# user signup route function
@main.route('/signup', methods=['POST', 'GET'])
def signup():
    """
        Handle user signup process.

        If the request method is POST, it checks the form data to create a new user account.
        It validates the email to ensure it is a valid Moringa School email and assigns a role accordingly.
        If the signup is successful, the user is redirected to the dashboard.
        If the signup fails, appropriate flash messages are shown.

        Returns:
            redirect: Redirects the user to different routes based on the signup result.
    """
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
                if result[1] == "student.moringaschool.com" or result[1] == "moringaschool.com":
                    if result[1] == "moringaschool.com":
                        role = 'staff'
                    else:
                        role = 'student'
                    new_user = User(name, email, generate_password_hash(password), role)
                    db.session.add(new_user)
                    db.session.commit()
                    session['username'] = name
                    session['email'] = email
                    session['password'] = password
                    return redirect(url_for('main.dashboard', username=new_user.name), code=307)
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
    """
        Handle user login process.

        If the request method is POST, it checks the form data to authenticate the user.
        If the login is successful, the user is redirected to the dashboard.
        If the login fails (e.g., wrong password or email not found), appropriate flash messages are shown.

        Returns:
            redirect: Redirects the user to different routes based on the login result.

    """
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
                if result[1] == "student.moringaschool.com" or result[1] == "moringaschool.com":
                    return redirect(url_for('main.dashboard', username=user.name), code=307)
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
    """
        Handle user sharing functionality.

        If the request method is POST, it allows users to share content in different categories (feedback, questions, shoutouts).
        The shared content is stored in the database with the corresponding category.
        If the sharing process is successful, the user is redirected to the dashboard.

        Returns:
            redirect: Redirects the user to different routes based on the sharing result.
    """
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
    """
        Handle commenting on feedback.

        If the request method is POST, it allows users to comment on specific feedback.
        The comment is stored in the database with the corresponding feedback ID.
        If the comment is successful, the user is redirected to the dashboard.

        Args:
            feedback_id (int): The ID of the feedback being commented on.

        Returns:
            redirect: Redirects the user to the dashboard.
    """
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
    """
        Handle commenting on questions.

        If the request method is POST, it allows users to comment on specific questions.
        The comment is stored in the database with the corresponding question ID.
        If the comment is successful, the user is redirected to the dashboard.

        Args:
            question_id (int): The ID of the question being commented on.

        Returns:
            redirect: Redirects the user to the dashboard.
    """
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
    """
        Handle commenting on shoutouts.

        If the request method is POST, it allows users to comment on specific shoutouts.
        The comment is stored in the database with the corresponding shoutout ID.
        If the comment is successful, the user is redirected to the dashboard.

        Args:
            shoutout_id (int): The ID of the shoutout being commented on.

        Returns:
            redirect: Redirects the user to the dashboard.
    """
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


from flask import render_template, redirect, url_for, request, session
from . import main
from ..models import Feedback, FeedbackComment, Question, QuestionComment, ShoutOut, ShoutOutComment, User


@main.route('/')
def home():
    """
        Handle requests to the root URL ('/') of the web application.

        If the user is logged in (i.e., the 'username' key is present in the session), 
        redirect the user to the dashboard page with their username as a parameter.

        If the user is not logged in, render the 'index.html' template as the home page.

        Returns:
            If logged in:
                Redirect response: Redirects the user to the dashboard page with their username.
            If not logged in:
                HTML page response: Renders the 'index.html' template as the home page.
    """
    if 'username' in session:
        return redirect(url_for('main.dashboard', username=session['username']))
    else:
        return render_template('index.html')


@main.route('/user/<username>', methods=['POST', 'GET'])
def dashboard(username):
    """
        Handle requests to the user dashboard page.

        This function retrieves various data related to the user's dashboard, including:
            - Information about the specified user from the database.
            - A list of all users from the database.
            - A list of all questions from the database.
            - A list of all feedback items from the database.
            - A list of all shoutouts from the database.
            - A list of all comments on feedback items from the database.
            - A list of all comments on questions from the database.
            - A list of all comments on shoutouts from the database.

        Parameters:
            username (str): The username of the user whose dashboard is being accessed.

        Returns:
            This function may render the retrieved data in an appropriate template or use it to
            perform other actions specific to the user dashboard page.
    """
    user = User.query.filter_by(name=username).first()
    users = User.query.all()
    questions = Question.query.all()
    feedback = Feedback.query.all()
    shoutouts = ShoutOut.query.all()

    feedback_comments = FeedbackComment.query.all()
    questions_comments = QuestionComment.query.all()
    shoutout_comments = ShoutOutComment.query.all()

    if not len(questions)!= 0:
        questions = 'empty'
    else:
        questions.reverse()

    if not len(feedback)!= 0:
        feedback = 'empty'
    else:
        feedback.reverse()

    if not len(shoutouts) != 0:
        shoutouts = 'empty'
    else:
        shoutouts.reverse()

    if not len(feedback_comments) != 0:
        feedback_comments = 'empty'
    else:
        feedback_comments.reverse()

    if not len(questions_comments) != 0:
        questions_comments = 'empty'
    else:
        questions_comments.reverse()

    if not len(shoutout_comments) != 0:
        shoutout_comments = 'empty'
    else:
        shoutout_comments.reverse()


    if user:
        return render_template(
            'user.html', user=user, users=users, questions=questions, feedback=feedback, 
            shoutouts=shoutouts, f_comments=feedback_comments, q_comments=questions_comments, 
            s_comments=shoutout_comments 
            )
    else:
        return redirect(url_for('main.home'))
    

@main.route('/logout')
def sign_out():
    """
        Handle the sign-out functionality for the web application.

        This function clears the session data, effectively logging out the user.
        After clearing the session, the user is redirected to the home page.

        Returns:
            Redirect response: Redirects the user to the home page after successfully signing out.
    """
    session.clear()
    return redirect(url_for('main.home'))




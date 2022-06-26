from flask import render_template, redirect, url_for, request, session
from . import main
from ..models import Feedback, FeedbackComment, Question, QuestionComment, ShoutOut, ShoutOutComment, User


@main.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('main.dashboard', username=session['username']))
    else:
        return render_template('index.html')


@main.route('/user/<username>', methods=['POST', 'GET'])
def dashboard(username):
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
    if not len(questions_comments) != 0:
        questions_comments = 'empty'
    if not len(shoutout_comments) != 0:
        shoutout_comments = 'empty'


    if user:
        return render_template(
            'user.html', user=user, users=users, questions=questions, feedback=feedback, 
            shoutouts=shoutouts, f_comments=feedback_comments, q_comments=questions_comments, 
            s_comments=shoutout_comments 
            )
    else:
        return redirect(url_for('main.home'))



@main.route('/staff/<username>', methods=['POST', 'GET'])
def staff_dashboard(username):
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
    if not len(feedback)!= 0:
        feedback = 'empty'
    if not len(shoutouts) != 0:
        shoutouts = 'empty'

    if not len(feedback_comments) != 0:
        feedback_comments = 'empty'
    if not len(questions_comments) != 0:
        questions_comments = 'empty'
    if not len(shoutout_comments) != 0:
        shoutout_comments = 'empty'

        
    if user:
        return render_template(
            'staff.html', user=user, users=users, questions=questions, feedback=feedback, 
            shoutouts=shoutouts, f_comments=feedback_comments, q_comments=questions_comments, 
            s_comments=shoutout_comments 
            )
    else:
        return redirect(url_for('main.home'))


    

@main.route('/logout')
def sign_out():
    session.clear()
    return redirect(url_for('main.home'))




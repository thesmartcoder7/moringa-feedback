from . import  db

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('FeedbackComment', backref='feedback', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='feedback', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='feedback', lazy='dynamic')

    def __str__(self) -> str:
        return self.content



class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('QuestionComment', backref='question', lazy='dynamic')
    # upvotes = db.relationship('Upvote', backref='question', lazy='dynamic')
    # downvotes = db.relationship('Downvote', backref='question', lazy='dynamic')

    def __str__(self) -> str:
        return self.content



class ShoutOut(db.Model):
    __tablename__ = 'shoutouts'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('ShoutOutComment', backref='shoutout', lazy='dynamic')
    # upvotes = db.relationship('Upvote', backref='shoutout', lazy='dynamic')
    # downvotes = db.relationship('Downvote', backref='shoutout', lazy='dynamic')

    def __str__(self) -> str:
        return self.content




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self) -> str:
        return self.name


class FeedbackComment(db.Model):
    __tablename__ = 'feedback-comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'))
    comment = db.Column(db.Text, nullable=False)



class QuestionComment(db.Model):
    __tablename__ = 'question-comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    comment = db.Column(db.Text, nullable=False)



class ShoutOutComment(db.Model):
    __tablename__ = 'shoutout-comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    shoutout_id = db.Column(db.Integer, db.ForeignKey('shoutouts.id'))
    comment = db.Column(db.Text, nullable=False)



class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=0)
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'))
    # question_id = db.column(db.Integer, db.ForeignKey('questions.id'))
    # shoutout_id = db.column(db.Integer, db.ForeignKey('shoutouts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default=0)
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'))
    # question_id = db.column(db.Integer, db.ForeignKey('questions.id'))
    # shoutout_id = db.column(db.Integer, db.ForeignKey('shoutouts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
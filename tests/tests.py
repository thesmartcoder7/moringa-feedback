import unittest
from app.models import Feedback, User, Comment, Upvote, Downvote, Question, ShoutOut


class FeedbackTest(unittest.TestCase):
    def setUp(self):
        self.new_feedback = Feedback(category='popote', content='popote is taking forever')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_feedback, Feedback))



class QuestionTest(unittest.TestCase):
    def setUp(self):
        self.new_question = Question(category='popote', content='why is popote taking too long?')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_question, Question))
    


class ShoutOutTest(unittest.TestCase):
    def setUp(self):
        self.new_shout_out = ShoutOut(category='maryann', content='shou out to maryann for not knowing how to give up on her students')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_shout_out, ShoutOut))



class UserTest(unittest.TestCase):
    def setUp(self):
        self.sam = User( 'samuel@martins.com', 'samuel', 'simplepass')

    def test_instance(self):
        self.assertTrue(isinstance(self.sam, User))



class CommentTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(user_id=10, feedback_id=10, comment="sample comment")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))



class UpVoteTest(unittest.TestCase):
    def setUp(self):
        self.up_vote = Upvote(user_id=10, feedback_id=10, upvote=5)

    def test_instance(self):
        self.assertTrue(isinstance(self.up_vote, Upvote))



class DownVoteTest(unittest.TestCase):
    def setUp(self):
        self.down_vote = Downvote(user_id=10, feedback_id=10, downvote=5)

    def test_instance(self):
        self.assertTrue(isinstance(self.down_vote, Downvote))


if __name__ == "__main__":
    unittest.main()

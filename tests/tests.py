import unittest
from app.models import Feedback, User, FeedbackComment, QuestionComment, ShoutOutComment, Upvote, Downvote, Question, ShoutOut


class FeedbackTest(unittest.TestCase):
    def setUp(self):
        self.new_feedback = Feedback(category='popote', content='popote is taking forever', topic='popote')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_feedback, Feedback))



class QuestionTest(unittest.TestCase):
    def setUp(self):
        self.new_question = Question(category='popote', content='why is popote taking too long?', topic='popote')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_question, Question))
    


class ShoutOutTest(unittest.TestCase):
    def setUp(self):
        self.new_shout_out = ShoutOut(category='maryann', content='shou out to maryann for not knowing how to give up on her students', topic='technical mentor')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_shout_out, ShoutOut))



class UserTest(unittest.TestCase):
    def setUp(self):
        self.sam = User( 'samuel@martins.com', 'samuel', 'simplepass')

    def test_instance(self):
        self.assertTrue(isinstance(self.sam, User))



class FeedbackCommentTest(unittest.TestCase):
    def setUp(self):
        self.new_fcomment = FeedbackComment(feedback_user_id=10, feedback_id=10, comment="sample comment")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_fcomment, FeedbackComment))



class QuestionCommentTest(unittest.TestCase):
    def setUp(self):
        self.new_qcomment = QuestionComment(question_user_id=10, question_id=10, comment="sample comment")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_qcomment, QuestionComment))



class ShoutOutCommentTest(unittest.TestCase):
    def setUp(self):
        self.new_scomment = ShoutOutComment(shoutout_user_id=10, shoutout_id=10, comment="sample comment")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_scomment, ShoutOutComment))



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

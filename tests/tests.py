import unittest
from app.models import Feedback, User, Comment, Upvote, Downvote


class FeedbackTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_feedback = Feedback(category='popote', content='popote is taking forever')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_feedback, Feedback))


class UserTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.sam = User( 'samuel@martins.com', 'samuel', 'simplepass')

    def test_instance(self):
        self.assertTrue(isinstance(self.sam, User))


class CommentTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_comment = Comment(user_id=10, pitch_id=10, comment="sample comment")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))


class UpVoteTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.up_vote = Upvote(user_id=10, pitch_id=10, upvote=5)

    def test_instance(self):
        self.assertTrue(isinstance(self.up_vote, Upvote))


class DownVoteTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.down_vote = Downvote(user_id=10, pitch_id=10, downvote=5)

    def test_instance(self):
        self.assertTrue(isinstance(self.down_vote, Downvote))


if __name__ == "__main__":
    unittest.main()

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        Test that was_published_recently() returns false for 
        posts published with future dates
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        Test that was_published_recently() returns false for 
        posts published with old dates more than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        Test that was_published_recently() returns false for
        post published with recent dates less than 1 dat
        """
        time = timezone.now() - datetime.timedelta(
                                    hours=23,
                                    minutes=59,
                                    seconds=59
                                )
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
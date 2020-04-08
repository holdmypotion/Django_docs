import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Database storing questions"""
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('published date')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """Database for storing choices to questions"""
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices",
        related_query_name="choices"
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choices
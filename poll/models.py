from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question

class Option(models.Model):
    option = models.CharField(max_length=500)
    number_of_vote = models.IntegerField(default=0)
    poll_question = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return self.option
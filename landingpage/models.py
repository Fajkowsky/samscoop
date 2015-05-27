from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):
    item_id = models.CharField(max_length=5)
    question = models.TextField()

class Answer(models.Model):
    child_number = models.CharField(max_length=9, default='')
    question_id = models.ForeignKey('Questions')
    yes_no = models.BooleanField()
    ages = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, default=1)

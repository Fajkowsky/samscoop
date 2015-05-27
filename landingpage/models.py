from django.db import models


class Questions(models.Model):
    item_id = models.CharField(max_length=5)
    question = models.TextField()

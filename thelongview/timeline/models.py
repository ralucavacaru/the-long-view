from django.db import models

class Event(models.Model):
    title = models.CharField(max_length = 500)
    year = models.IntegerField();
    identifier = models.CharField(max_length = 20)
    description = models.TextField()
    full_story = models.TextField()
    why = models.TextField()
    impacts = models.TextField()
    article = models.TextField(default="")


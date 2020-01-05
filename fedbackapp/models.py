from django.db import models

class FeedbackData(models.Model):
    name=models.CharField(max_length=30)
    rating=models.IntegerField()
    feedback=models.CharField(max_length=100)
    date=models.DateTimeField(max_length=30)



from django.db import models
from django.contrib.auth.models import AbstractUser
class Review(models.Model):
    """Review model"""
    id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    content = models.CharField(max_length=100, blank=True)
    reviewer = models.IntegerField()
    reviewee = models.IntegerField()
    trip = models.IntegerField()
    class Meta:
        app_label = 'reviews_app'


    def __str__(self):
        return str(self.id) + " " + str(self.score) + " from " + str(self.reviewer) + " to " + str(self.reviewee) + " on " + str(self.trip)



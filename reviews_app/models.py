
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Review(models.Model):
    """Review model"""
    id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    content = models.CharField(max_length=100, blank=True)
    reviewer = models.IntegerField()
    reviewee = models.IntegerField()
    trip = models.IntegerField()
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)

    class Meta:
        app_label = 'reviews_app'

    def __str__(self):
        return f"Review {self.id} for trip {self.trip} by user {self.reviewer}"

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                f"score-{self.score}_reviewer-{self.reviewer}_reviewee-{self.reviewee}_trip-{self.trip}")
        super().save(*args, **kwargs)

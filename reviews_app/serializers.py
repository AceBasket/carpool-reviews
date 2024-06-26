from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""
    class Meta:
        """Meta class for ReviewSerializer"""
        model = Review
        exclude = ['slug']
        lookup_field = 'slug'

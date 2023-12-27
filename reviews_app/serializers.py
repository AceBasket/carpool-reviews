from rest_framework import serializers

from .models import Review
class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""
    review_trip_date = serializers.ReadOnlyField(source='trip.date')
    review_trip_car = serializers.ReadOnlyField(source='trip.car.license_plate')
    class Meta:
        """Meta class for ReviewSerializer"""
        model = Review
        fields = ['id', 'score', 'content', 'reviewer', 'reviewee', 'trip', 'review_trip_date', 'review_trip_car']


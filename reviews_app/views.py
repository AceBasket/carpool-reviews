from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ReviewSerializer
from rest_framework import permissions
from .models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'

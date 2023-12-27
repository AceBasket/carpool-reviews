from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ReviewSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics  # Add this import statement
from .models import Review  # Add this import statement
# import producer.py at ../producer.py


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

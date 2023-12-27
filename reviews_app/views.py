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
    #permission_classes = [permissions.IsAuthenticated]
    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def update(self, request, pk=None):
        review = Review.objects.get(id=pk)
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def destroy(self, request, pk=None):
        review = Review.objects.get(id=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewAPIView(generics.GenericAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id):
        return self.destroy(request, id)
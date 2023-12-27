from rest_framework import routers
from reviews_app import views
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'reviews', views.ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

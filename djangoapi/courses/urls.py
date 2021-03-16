from django.urls import path, include
from . import views # . allows you to draw from the current directory
from rest_framework import routers # allows us to get and post requests

router = routers.DefaultRouter()
router.register('courses', views.CourseView) # this allows users to access api from /courses


urlpatterns = [
    path('', include(router.urls)),
    
]
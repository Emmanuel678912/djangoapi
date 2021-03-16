from django.shortcuts import render
from rest_framework import viewsets # create sets of pages
from .models import Course
from .serializers import CourseSerializer

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all() # what data do we get from the database
    serializer_class = CourseSerializer # what serializer class does it need to use

    
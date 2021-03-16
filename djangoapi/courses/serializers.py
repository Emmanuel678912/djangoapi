from rest_framework import serializers # django serializers take data from databases and changes them into JSON
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer): # HyperlinkedModelSerializer allows you to add a hyperlink
    class Meta: 
        model = Course # this tells it what model to use
        fields = ('id', 'url', 'name', 'language', 'price') # this tells the serializer what fields from the model to use

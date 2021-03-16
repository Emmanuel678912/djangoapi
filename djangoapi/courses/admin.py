from django.contrib import admin
from .models import Course

# Register your models here.
admin.site.register(Course) # this adds the course model to the admin section on localhost
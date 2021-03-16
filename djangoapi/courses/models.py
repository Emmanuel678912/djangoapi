from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name # this changes the course objects name from course objects to the models name

    # after building a model python manage.py makemigrations then python manage.py migrate
    # models are used to build databases
    # then go to the admin file in your app directory and import the model
    # then you type in admin.site.register and this adds the model to the admin section
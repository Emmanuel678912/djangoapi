from django.contrib import admin
from django.urls import path, include # allows you to include other files 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')), # includes courses urls in the app as the root directory
]


from django.urls import path, include
from .views import home, body, studentView

urlpatterns = [
    path('tmp', body), 
    path('home', home),
    path('student', studentView),
  
]

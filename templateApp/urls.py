
from django.urls import path, include
from .views import home, body

urlpatterns = [
    path('tmp', body), 
    path('home', home),
  
]

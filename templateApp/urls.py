
from django.urls import path, include
from .views import home, body, studentView, student_addView, StudentAddView, StudentListView

urlpatterns = [
    path('tmp', body), 
    path('home', home),
    path('student', studentView, name='student'), #bunun uniqe olmasi gerekiyor.
    #forms
    #fbv
    # path('add', student_addView),
    #cbv
    path('add',StudentAddView.as_view(), name='add'),
    path('list',StudentListView.as_view(), name='list')

]



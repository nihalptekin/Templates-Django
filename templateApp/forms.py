from django import forms 
from .models import Student
class StudentForm(forms.Form):
    class Meta:
        model=Student
        fields='__all__'


    


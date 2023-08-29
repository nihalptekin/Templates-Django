from django import forms 
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels={
            'first_name':'Adinizi giriniz',
            'gender':'Cinsiyet seçiniz.'
        }
        widgets={
            'gender': forms.RadioSelect
        }


    


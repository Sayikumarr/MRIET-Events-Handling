# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import Student
 
# create a ModelForm
class StudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        fields = "__all__"
 from django import forms
 from .models import Assignment

class Assignment(forms.ModelForm):\
    class Meta:
         model = Assignment
         fields = ['Assigned_To', 'Assigned_By']
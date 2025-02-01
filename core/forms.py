from django import forms
from core.models import StudentModel 

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name', 'email', 'phone', 'course']   
    
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}))
     


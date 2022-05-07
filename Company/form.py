from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
class passwordform(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')
        
        
# class addagentforms():
#     old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     class Meta:
#         model=User
#         fields=('old_password','new_password1','new_password2')
        
# # Create the form class.
# class ArticleForm(ModelForm):
#     class Meta:
#         model = Agent
#         fields = '__all__'

# class PostFormNew(forms.ModelForm):
#     class Meta:
#         model=Agent
#         fields='__all__'


class NameForm(forms.ModelForm):
    class Meta:
        model=Agent
        fields=('Region',)
        Widget = {'Region':forms.Select(attrs={'class':'form-control'}),}
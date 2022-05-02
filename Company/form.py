from tkinter import Widget
from django import forms
from .models import *

class AddAgentForm(forms.ModelForm):
    class Meta:
        model=Agent
        fields=('Agent_name',)
       
   
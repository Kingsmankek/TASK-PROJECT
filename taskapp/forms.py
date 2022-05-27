from dataclasses import field, fields
from pyexpat import model
from django import forms 
from . models import TaskModel

class TaskmodelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task',] 
        
        
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
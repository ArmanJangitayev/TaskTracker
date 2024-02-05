from django import forms

from Task.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'




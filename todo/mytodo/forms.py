from django import forms
from mytodo.models import Todo

class TodoForm(forms.ModelForm) :
    class Meta :
        model =Todo
        fields =['name', 'body', 'completed']

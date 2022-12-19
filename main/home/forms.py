from .models import Job
from django.forms import ModelForm, TextInput, Textarea


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'vocation', 't_number', 'href']

        widgets = {
            'name': TextInput(attrs={
                'class': 'name-control',
                'placeholder': 'Your name'
            }),
            'vocation': TextInput(attrs={
                'class': 'voc-control',
                'placeholder': 'Enter your vacancy'
            }),
            't_number': TextInput(attrs={
                'class': 'number-control',
                'placeholder': 'Enter your number'
            }),
            'href': TextInput(attrs={
                'class': 'href-control',
                'placeholder': 'Link to resume'
            }),
        }

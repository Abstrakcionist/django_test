from .models import Inputs
from django.forms import ModelForm, TextInput, DateInput, Textarea


class InputsForm(ModelForm):
    class Meta:
        model = Inputs
        fields = ['username', 'date_of_birth', 'info']

        widgets = {
            'username': TextInput(attrs={'placeholder': "Имя"}),
            'date_of_birth': DateInput(attrs={'placeholder': "Дата рождения"}),
            'info': Textarea(attrs={'placeholder': "Описание"}),
        }

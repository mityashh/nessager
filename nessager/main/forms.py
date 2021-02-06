from .models import Msgr
from django.forms import ModelForm, TextInput

class MsgrForm(ModelForm):
	class Meta:
		model = Msgr
		fields = ["name", "text"]
		widgets = {
			"name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Name'
			}),
			"text": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Text'
			})
		}
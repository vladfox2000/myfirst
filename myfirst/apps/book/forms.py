from .models import adress
from django.forms import ModelForm, TextInput


class adressForm(ModelForm):
	class Meta:
		model = adress
		fields = ["first_name", "second_name", "l_country", "l_city", "l_street", "phone_number"]
		widgets = {
			"first_name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ваша фамилия'
			}),
			"second_name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ваше имя'
			}),
			"l_country": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ваша страна'
			}),
			"l_city": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ваш город'
			}),
			"l_street": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ваша улица'
			}),
			"phone_number": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ваш телефон'
			}),

		}
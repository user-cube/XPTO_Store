from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Email


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class EmailForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, help_text='Your name is required.')
    email = forms.EmailField(max_length=254, help_text='Your email is required.')
    phone = forms.IntegerField()
    message = forms.CharField()

    class Meta:
        model = Email
        field = ('email', 'phone', 'message', 'name')
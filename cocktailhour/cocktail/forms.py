from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cocktail


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None) # Now you use self.request to access request object.
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password1']
        validators(password)
        return password


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CreateForm(forms.Form):
    class Meta:
        model =  Cocktail
        fields = ("info")

class EditForm(forms.Form):
    class Meta:
        model =  Cocktail
        fields = ("info")

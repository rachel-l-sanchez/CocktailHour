from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cocktail, UserProfile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None) # Now you use self.request to access request object.
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password1']
        validators(password)
        return password

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

class EditForm(forms.ModelForm):
    class Meta:
        model =  Cocktail
        fields = ("id", "drinkName", "ingredient1", "ingredient2", "measure1", "measure2")

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('favorites',)
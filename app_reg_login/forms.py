from django import forms
from django.forms import ModelForm, Form

from .models import User, Item, ImageTable
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'password1', 'password2', 'phone', 'address']
        # fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'phone', 'address']


class SellForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['seller', 'highest_price', 'participants']


class ImageForm(ModelForm):
    images = forms.FileField()

    class Meta:
        model = ImageTable
        fields = ['images']

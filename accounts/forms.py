from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile, Product
from products.models import *

from django.forms import ModelForm, ClearableFileInput


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "image",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["user", "image"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'brand', 'category']


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True})
        }

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile, OrderItem, User
from products.models import Product, Image
from django.forms import ModelForm, ClearableFileInput


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "address")
            
        def clean_username(self):
            username = self.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('아이디가 이미 사용중입니다')
            return username


class CustomUserChangeForm(UserChangeForm):
    class Meta():
        model = get_user_model()
        fields = (
            "username",
            "image",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile()
        fields = ["user", "image",]
        labels = {
            'image': '프로필 사진'
        }


# admin이 사용자의 구매상품 정보를 등록할 때의 form
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'brand', 'category']


# ClearableFileInput을 사용해서 여러 장의 이미지를 받음
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True})
        }
        

class ProductBuyForm(ModelForm):
    class Meta:
        model = Product
        fields = ['quantity']
        labels = {'quantity': '수량'}
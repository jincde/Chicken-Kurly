from django.forms import ModelForm, ClearableFileInput
from .models import *

# admin이 판매상품 정보를 등록할 때의 form
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'brand', 'category']

# 일반 user가 구매할 때 form (구매 수량만)
class ProductBuyForm(ModelForm):
    class Meta:
        model = Product
        fields = ['quantity']
        
# ClearableFileInput으로 여러 장의 image를 입력 받을 수 있음
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True})
        }

# 상품 문의 form
class InquiryForm(ModelForm):
    class Meta:
        model = Inquiry
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '내용',
        }

# 상품 문의에 대한 답변 form
class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': '내용',
        }
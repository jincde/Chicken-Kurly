from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def index(request):
    products = Product.objects.order_by('-pk')

    context = {
        'products': products,
        # 'image_cnt': products.image_set.count(), # index 페이지에서 carousel로 보여줄 때 사용
    }

    return render(request, 'products/index.html', context)

# admin의 판매 상품 등록
@login_required
def create(request):
    # 요청한 user의 is_superuser가 1이면(admin이면)
    if request.user.is_superuser == 1: 
        if request.method == 'POST':
            product_form = ProductForm(request.POST)
            # form에 image 폼 추가
            image_form = ImageForm(request.POST, request.FILES)
            images = request.FILES.getlist('image')
            
            # 상품 정보에 대한 폼과 이미지 폼이 유효하면
            if product_form.is_valid() and image_form.is_valid():
                product = product_form.save(commit=False)
                product.admin = request.user

                if images:
                    for img in images:
                        img_instance = Image(product=product, image=img)
                        product.save()
                        img_instance.save()

                product.save()
                messages.success(request, '상품 등록이 완료되었습니다.')
                return redirect('products:index')
        else:
            product_form = ProductForm()
            image_form = ImageForm()
            
        context = {
            'product_form': product_form,
            'image_form': image_form,
        }

        return render(request, 'products/create.html', context)
    
    else:
        return redirect('products:index')    # admin 아니면 index로 리다이렉트
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

def detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    # model에서 hit은 default=0으로 설정했고 한 번 볼 때마다 1 증가하도록
    product.hit += 1
    product.save()

    # 유저 회원가입 시 생성된 장바구니
    cart = Cart.objects.get(user=request.user)
    
    # 구매 수량 입력 후 장바구니
    if request.method == 'POST':
        product_buy_form = ProductBuyForm(request.POST)

        if product_buy_form.is_valid():
            form = product_buy_form.save()
            if 'cart' in request.POST:
                CartItem.objects.create(cart=cart, product=product, quantity=form.quantity)

    else:
        product_buy_form = ProductBuyForm()
    
    context = {
        'product': product,
        'image_cnt': product.image_set.count(),
        'product_buy_form': product_buy_form,
    }

    return render(request, 'products/detail.html', context)

# 찜
def ddib(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    ddib = Ddib.objects.get(user=request.user)

    DdibItem.objects.create(ddib=ddib, product=product)
    
    return redirect('products:detail', product_pk)
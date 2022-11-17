from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, ProfileForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from products.models import Cart, Ddib
from .models import OrderItem, WatchItem, Product, User, UserMember
from .forms import ImageForm, OrderItemForm
from django.contrib import messages
from .forms import ProductBuyForm
from products.models import *
from products.forms import *
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
from django.db.models import Q




# Create your views here.
def signup(request):
    if request.method == "POST":
        forms = SignupForm(request.POST, request.FILES)
        if forms.is_valid():
            user = forms.save()      
            Cart.objects.create(user=user)
            Ddib.objects.create(user=user)
            # UserDdib.objects.create(user=user)
            return redirect("articles:index")
    else:
        forms = SignupForm()
    context = {
        "forms": forms,
    }
    return render(request, "accounts/signup.html", context)

def isValidId(request):
    data = json.loads(request.body)
    username = data.get("username")
    print(data)

    if User.objects.filter(Q(username = data['username'])).exists():
        flag = 1
    else:
        flag = 0

    context = {
        "flag": flag,
        }
    return JsonResponse(context)

def index(request):
    members = get_user_model().objects.all()
    return render(request, "accounts/index.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "articles:index")
        messages.warning(request, '아이디, 비밀번호를 확인해주세요', extra_tags='')
    else:
        form = AuthenticationForm()
    context = {"forms": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:index")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            
            return redirect("accounts:profile", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        forms = PasswordChangeForm(request.user, request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("accounts:profile")
    else:
        forms = PasswordChangeForm(request.user)
    context = {
        "forms": forms,
    }
    return render(request, "accounts/change_password.html", context)


def profile(request, user_pk):
    products = Product.objects.order_by('-pk')
    ddib = Ddib.objects.get(user=request.user) # 요청한 사용자의 찜(가방)을 가져와라.
    ddib_items = ddib.ddibitem_set.all() # 찜한 목록(가방 안에 있는 물건들)을 가져와라.
    OrderItems = OrderItem.objects.order_by('-pk')
    order_items = OrderItem.objects.filter(user=request.user)
    watch_items = WatchItem.objects.filter(user=request.user)
    user = get_user_model().objects.get(pk=user_pk)
    inquiries = user.inquiry_set.order_by('-pk')
    usermember = UserMember.objects.get(pk=user_pk)

    
    
    reply_form = ReplyForm()
    person = get_user_model()
    person = get_object_or_404(person, pk=user_pk)
    product_buy_form = ProductBuyForm() 
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    # 문의 페이지네이션
    inquiry_page = request.GET.get('inquiry_page', '1')
    inquiry_paginator = Paginator(inquiries, 5)
    inquiry_page_obj = inquiry_paginator.get_page(inquiry_page)

    context = {
        "OrderItems": OrderItems,
        "person": person,
        "ddib_items": ddib_items,
        'product_buy_form': product_buy_form,
        'order_items': order_items,
        'watch_items': watch_items,

        'cart_items': cart_items,
        'inquiries': inquiries,
        'reply_form': reply_form,
        'inquiries': inquiry_page_obj,
        'usermember': usermember,
        }
    return render(request, "accounts/profile.html", context)

# 찜한 상품 삭제
def ddib_delete(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    ddib = Ddib.objects.get(user=request.user) # user와 ddib 1:1
    ddib_items = ddib.ddibitem_set.all()

    for item in ddib_items:
        if product == item.product:
            item.delete()
            break
    return redirect('accounts:profile', request.user.pk)

@login_required
def profile_update(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        forms = PasswordChangeForm(request.user, request.POST)
        if form and forms.is_valid():
            form.save()
            forms.save()
            return redirect("accounts:profile", request.user.pk)
    else:
        form = ProfileForm(instance=request.user)
        forms = PasswordChangeForm(request.user)
    return render(
        request,
        "accounts/profile_update.html",
        {
            "form": form,
            "forms": forms,
        },
    )


@login_required
def follow(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
        return redirect("accounts:profile", user_pk)
    else:
        return HttpResponseForbidden()


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:login")


# admin의 판매 상품 등록
@login_required
def create(request):
    # 요청한 user의 is_superuser가 1이면(admin이면)
    if request.user.is_superuser == 1: 
        if request.method == 'POST':
            OrderItem_form = OrderItemForm(request.POST, request.FILES)
            # form에 image 폼 추가      
            # 상품 정보에 대한 폼과 이미지 폼이 유효하면
            if OrderItem_form.is_valid():
                OrderItem = OrderItem_form.save(commit=False)
                OrderItem.admin = request.user
                OrderItem.user = request.user
                OrderItem.save()
                messages.success(request, '상품 등록이 완료되었습니다.')
                return redirect('accounts:profile', request.user.pk)
        else:
            OrderItem_form = OrderItemForm()         
        
        context = {
            'OrderItem_form': OrderItem_form,
        }

        return render(request, 'accounts/create.html', context)
    
    else:
        return redirect('products:index')    # admin 아니면 index로 리다이렉트


# 로그인한 유저의 장바구니 페이지
@login_required
def cart(request):
    cart = Cart.objects.get(user=request.user)

    cart_items = cart.cartitem_set.all()
    
    # 장바구니 기본이 checked일 때
    # total_price = 0
    # for item in cart_items:
    #     total_price += item.product.price * item.quantity

    context = {
        'cart_items': cart_items,
        # 'total_price': total_price,
    }

    return render(request, 'accounts/cart.html', context)


# 장바구니에서 구매 & 삭제
@login_required
def cart_update(request):
    cart = Cart.objects.get(user=request.user)
    selected_items = request.POST.getlist('selected_items') # 선택된 아이템들의 product_pk 리스트
    quantities = request.POST.getlist('quantities') # 선택된 아이템들의 quantity 리스트
    
    # print(request.POST)
    deleted_item_pk_list = []
    
    # axios 아니면 그냥 request.POST로 해도 OK
    if 'purchase' in request.POST.get('kindOfSubmit'):
        # 선택된 아이템의 개수만큼 반복
        for i in range(len(selected_items)):
            # 1. 선택된 장바구니 아이템의 pk로 아이템 인스턴스 객체를 가져옴.
            cart_item = cart.cartitem_set.get(pk=selected_items[i])
            # 2. 장바구니 페이지에서 수정된 수량으로 변경
            quantity = quantities[i]
            
            # 위 2개의 정보를 바탕으로 주문서 작성
            OrderItem.objects.create(ordered=True, product=cart_item.product, quantity=quantity, user=request.user)
            cart_item.product.sold_count += 1
            cart_item.product.save()
    
    elif 'select_delete' in request.POST.get('kindOfSubmit'):
        for i in range(len(selected_items)):
            # 선택된 장바구니 아이템의 pk로 아이템 인스턴스 객체를 가져옴.
            cart_item = cart.cartitem_set.get(pk=selected_items[i])
            cart_item.delete()
            deleted_item_pk_list.append(selected_items[i])
    
    elif 'delete' in request.POST.get('kindOfSubmit'):
        product_pk = request.POST.get('productPk')
        cart_item = cart.cartitem_set.get(pk=product_pk)
        cart_item.delete()
        deleted_item_pk_list.append(product_pk)

    data = {
        'deletedItemList': deleted_item_pk_list,
    }

    # return redirect('accounts:cart')
    return JsonResponse(data, safe=False)

def tocart(request, product_pk):
    product = Product.objects.get(pk=product_pk)

    if request.method == 'POST':
        cartitem = CartItem()
        cartitem.quantity = request.POST['checkquantity']
       
        cartitem.cart = Cart.objects.get(pk=request.user.pk)
        cartitem.product = product
        
        cartitem.save()
        
    return redirect('accounts:cart')


def payment(request):
    print('###########', request.POST)
    selected_items = request.POST.getlist('selected_items') # 선택된 아이템들의 product_pk 리스트
    quantities = request.POST.getlist('quantities') # 선택된 아이템들의 quantity 리스트
    print(selected_items)
    print(quantities)
    
    return redirect('accounts:cart')
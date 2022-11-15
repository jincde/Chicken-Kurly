from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, ProfileForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from products.models import Cart, Ddib, Product

from .forms import ImageForm, ProductForm
from django.contrib import messages
from products.models import Image


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


def index(request):
    members = get_user_model().objects.all()
    return render(request, "accounts/index.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "articles:index")
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
        forms = CustomUserChangeForm(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
            
            return redirect("accounts:profile", request.user.pk)
    else:
        forms = CustomUserChangeForm(instance=request.user)
    context = {
        "forms": forms,
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
    
    person = get_user_model()
    person = get_object_or_404(person, pk=user_pk)
    context = {
        "products": products,
        "person": person,
        "ddib_items": ddib_items
    }
    return render(request, "accounts/profile.html", context)


@login_required
def profile_update(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile", request.user.pk)
    else:
        form = ProfileForm(instance=request.user)
    return render(
        request,
        "accounts/profile_update.html",
        {
            "form": form,
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
            product_form = ProductForm(request.POST)
            # form에 image 폼 추가
            image_form = ImageForm(request.POST, request.FILES)
            tmp_images = request.FILES.getlist('image')
            
            # 상품 정보에 대한 폼과 이미지 폼이 유효하면
            if product_form.is_valid() and image_form.is_valid():
                product = product_form.save(commit=False)
                product.admin = request.user

                if tmp_images:
                    for img in tmp_images:
                        img_instance = Image(product=product, image=img)
                        product.save()
                        img_instance.save()

                product.save()
                messages.success(request, '상품 등록이 완료되었습니다.')
                return redirect('accounts:profile', request.user.pk)
        else:
            product_form = ProductForm()
            image_form = ImageForm()
            
        context = {
            'product_form': product_form,
            'image_form': image_form,
        }

        return render(request, 'accounts/create.html', context)
    
    else:
        return redirect('products:index')    # admin 아니면 index로 리다이렉트

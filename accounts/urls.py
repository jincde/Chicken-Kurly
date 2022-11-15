from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("change_password/", views.change_password, name="change_password"),
    path("<int:user_pk>/", views.profile, name="profile"),
    path("profile_update/", views.profile_update, name="profile_update"),
    path("delete/", views.delete, name="delete"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path('create/', views.create, name='create'),
    path('cart/', views.cart, name='cart'), # 장바구니 페이지
    path('cart/purchase/', views.cart_purchase, name='cart_purchase'), # 장바구니 업데이트
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

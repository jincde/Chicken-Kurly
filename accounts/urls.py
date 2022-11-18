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
    path("<int:user_pk>/", views.profile, name="profile"),
    path("profile_update/", views.profile_update, name="profile_update"),
    path("delete/", views.delete, name="delete"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path(
        "change_password/", views.change_password, name="change_password"
    ),
    path('cart/', views.cart, name='cart'), # 장바구니 페이지
    path('cart/update/', views.cart_update, name='cart_update'), # 장바구니 구매 및 삭제
    path('cart/payment/', views.payment, name='payment'),
    path('<int:product_pk>/ddib_delete/', views.ddib_delete, name='ddib_delete'), # 프로필에서 찜한 상품(product_pk) 삭제
    path('<int:product_pk>/tocart/', views.tocart, name='tocart'), # 찜한 상품 모달에서 수량 선택 후 장바구니로 담기
    path('isValidId/', views.isValidId, name='isValidId'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

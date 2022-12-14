from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:product_pk>/', views.detail, name='detail'),
    path('<int:product_pk>/update/', views.update, name='update'),
    path('<int:product_pk>/ddib/', views.ddib, name='ddib'),
    path('<int:product_pk>/cart/', views.cart, name='cart'),
    path('<int:product_pk>/review_create/', views.review_create, name='review_create'),
    path('<int:product_pk>/<int:review_pk>/review_update/', views.review_update, name='review_update'),
    path('<int:product_pk>/inquiry/', views.create_inquiry, name='create_inquiry'),   # 문의 등록
    path('<int:product_pk>/inquiry/<int:inquiry_pk>/update/', views.update_inquiry, name='update_inquiry'),   # 문의 수정
    path('<int:product_pk>/inquiry/<int:inquiry_pk>/delete/', views.delete_inquiry, name='delete_inquiry'),   # 문의 삭제
    path('<int:product_pk>/inquiry/<int:inquiry_pk>/reply/', views.create_reply, name='create_reply'),   # 답변 등록
    path('<int:product_pk>/payment/', views.payment, name='payment'),
]

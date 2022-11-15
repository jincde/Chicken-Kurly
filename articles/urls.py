from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
    path("comment/<int:pk>/", views.c_create, name="c_create"),
    path("comment/<int:c_pk>/delete/<int:a_pk>", views.c_delete, name="c_delete"),
    path("like/<int:pk>/", views.like, name="like"),
    path("c_like/<int:c_pk>/<int:a_pk>", views.c_like, name="c_like"),
    path("rc_create/<int:c_pk>/<int:a_pk>", views.rec_create, name="rec_create"),
] 

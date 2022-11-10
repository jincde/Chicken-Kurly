from django.urls import path
from . import views

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
]

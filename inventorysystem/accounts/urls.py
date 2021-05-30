from django.contrib.auth import views
from django.urls import path
from . import views as v

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('', views.LoginView.as_view(), name='accounts-logout'),
    path("register", v.register, name="register"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.UserRegisterView.as_view(), name='User_Register'),
]

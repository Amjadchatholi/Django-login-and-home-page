from django.urls import path

from app1 import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.signin, name="login"),
    path('logout/', views.signout, name="logout")
   
]


from django.urls import path
from django.contrib import admin

from App import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about_us', views.Aboutus, name = 'about'),
    path('log_in', views.Login, name = 'login'),
    path('register', views.Signup, name = 'sign'),
    path('index' ,views.Index, name= 'index'),
    path('product_single/<int:id>',views.get_products,name="product_detail"),
    path('search/',views.Search,name="search")
]
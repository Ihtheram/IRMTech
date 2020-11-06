from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('detail/', views.detail, name="detail"),
    path('orders/', views.orders, name="orders"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]
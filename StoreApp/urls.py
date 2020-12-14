from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('devices/', views.devices, name="devices"),
	path('softwares/', views.softwares, name="softwares"),
	path('<int:techId>/detail', views.detail, name='detail'),
    path('orders/', views.orders, name="orders"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),

    path('add_tech/', views.addTech, name="add_tech"),    
    path('manage_techs/', views.manageTechs, name="manage_techs"),
    path('<int:techId>/update_tech/', views.updateTech, name="update_tech"),
    path('<int:techId>/delete_tech/', views.deleteTech, name="delete_tech"),

   	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
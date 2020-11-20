from django.shortcuts import get_object_or_404, render, redirect
from .models import PERSON, TECH, OrderInfo, OrderedTech, DeliveryLocation

import json
from django.http import JsonResponse, HttpResponse, Http404

from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView



def store(request):

    if request.user.is_authenticated:
        person=request.user.person
        order, created = OrderInfo.objects.get_or_create(customer=person, complete=False)
        items= order.orderedtech_set.all()
        cartItems = order.get_cart_items
    else:
        person = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        order = {'get_cart_items':0, 'shipping':False}
        items = []
        cartItems = order['get_cart_items']

    techs = TECH.objects.all()
    context = {'person':person, 'techs':techs, 'items':items,'order':order}
    return render(request, 'StoreApp/store.html',context)



def detail(request, techId):

    if request.user.is_authenticated:
        person=request.user.person
        order, created = OrderInfo.objects.get_or_create(customer=person, complete=False)
        items = order.orderedtech_set.all()
    else:
        person = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        items = []

    try:
        this_tech = TECH.objects.get(id=techId)
    except TECH.DoesNotExist:
        raise Http404("Tech does not exist")

    context = {'person':person, 'this_tech': this_tech, 'items':items,'order':order}
    return render(request, 'StoreApp/detail.html',context)



def orders(request):

    if request.user.is_authenticated:
        person=request.user.person
        order, created = OrderInfo.objects.get_or_create(customer=person, complete=False)
        items = order.orderedtech_set.all()
    else:
        person = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        items = []

    context = {'person':person, 'items':items,'order':order}
    return render(request, 'StoreApp/orders.html',context)



def cart(request):

    if request.user.is_authenticated:
        person=request.user.person
        order, created = OrderInfo.objects.get_or_create(customer=person, complete=False)
        items = order.orderedtech_set.all()
    else:
        person = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        items = []

    context = {'person':person, 'items':items,'order':order}
    return render(request, 'StoreApp/cart.html',context)



def checkout(request):
    
    if request.user.is_authenticated:
        person=request.user.person
        order, created = OrderInfo.objects.get_or_create(customer=person, complete=False)
        items = order.orderedtech_set.all()
    else:
        person = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        items = []

    context = {'person':person, 'items':items,'order':order}
    return render(request, 'StoreApp/checkout.html',context)

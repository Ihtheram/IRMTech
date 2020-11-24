from django.shortcuts import get_object_or_404, render, redirect
from .models import PERSON, TECH, OrderInfo, OrderedTech, DeliveryLocation
import datetime

import json
from django.http import JsonResponse, HttpResponse, Http404

from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from .forms import TechForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



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
        orderedtechs = OrderedTech.objects.all()

    else:
        person = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        items = []
        orderedtechs = []
    


    context = {'person':person, 'items':items,'order':order, 'orderedtechs':orderedtechs}
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



def updateItem(request):

    user = request.user.person
    order, created = OrderInfo.objects.get_or_create(customer=user, complete=False)
    
    data = json.loads(request.body)
    techId = data['techId']
    tech = TECH.objects.get(id=techId)
    
    orderedTech, created = OrderedTech.objects.get_or_create(order=order, tech=tech) 
    
    action = data['action']
    if action == 'add':
        orderedTech.quantity = (orderedTech.quantity + 1)
    elif action == 'remove':
        orderedTech.quantity = (orderedTech.quantity - 1)

    orderedTech.save()

    if orderedTech.quantity <= 0:
        orderedTech.delete()

    return JsonResponse('Item was added', safe=False)


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		user = request.user.person
		order, created = OrderInfo.objects.get_or_create(customer=user, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id

		if total == order.get_cart_total:
			order.complete = True
		order.save()

		if order.shipping == True:
			DeliveryLocation.objects.create(
				customer=user,
				order=order,
				address=data['shipping']['address'],
				city=data['shipping']['city'],
				state=data['shipping']['state'],
				zipcode=data['shipping']['zipcode'],
			)

	else:
		print('User is not logged in..')
	return JsonResponse('Payment complete!', safe=False)


def signup(request):

    if request.user.is_authenticated:
        user=request.user.person
        order, created = OrderInfo.objects.get_or_create(customer=user, complete=False)
        items= order.orderedtech_set.all()
        cartItems = order.get_cart_items
    else:
        user = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
		}
        order = {'get_cart_items':0, 'shipping':False}
        items = []
        cartItems = order['get_cart_items']

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {
			'items': items, 'order': order, 'user': user,'form':form
	})

from django.core.files.storage import FileSystemStorage
def addTech(request):

    form = TechForm()
    
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



    if request.method == 'POST':
        #to see what info are input, in console, uncomment the line below
        #print('Printing POST:', request.POST)
        form = TechForm(request.POST, request.FILES)
        # uploaded_image = request.FILES('document')
        # fss = FileSystemStorage()
        # imagename = fss.save(uploaded_image.name, uploaded_image)
        # context['image']=fss.url(imagename)
        

        if form.is_valid():
            form.save()
            return redirect('manage_techs')  

    techs = TECH.objects.all()
    context = {'form':form, 'person':person, 'techs':techs, 'items':items,'order':order}

    return render(request, 'StoreApp/addtech.html',context)



def manageTechs(request):

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
    return render(request, 'StoreApp/managetechs.html',context)


def updateTech(request, techId):
    form = TechForm()
    tech = TECH.objects.get(id=techId)
    form = TechForm(instance=tech)

    if request.method == 'POST':
        #to see what info are input, in console, uncomment the line below
        #print('Printing POST:', request.POST)
        form = TechForm(request.POST, instance=tech)
        if form.is_valid():
            form.save()
            return redirect('manage_techs')

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

    context = {'form':form, 'person':person, 'this_tech': this_tech, 'items':items,'order':order}
    return render(request, 'StoreApp/updatetech.html',context)


def deleteTech(request, techId):

    try:
        this_tech = TECH.objects.get(id=techId)
    except TECH.DoesNotExist:
        raise Http404("Tech does not exist")

    if request.method == 'POST':
        this_tech.delete()
        return redirect('manage_techs')
    
    context = {'this_tech': this_tech}
    return render(request, 'StoreApp/deletetech.html',context)
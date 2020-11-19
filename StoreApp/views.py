from django.shortcuts import render
from .models import PERSON, TECH

def store(request):

    if request.user.is_authenticated:
        User=request.user.person
    else:
        User = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
    tech = TECH.objects.all()
    context = {'techs':tech, 'User':User}
    return render(request, 'StoreApp/store.html',context)

def detail(request, techId):

    if request.user.is_authenticated:
        User=request.user.person
    else:
        User = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
    try:
        this_tech = TECH.objects.get(id=techId)
    except TECH.DoesNotExist:
        raise Http404("Tech does not exist")
    context = {'User':User, 'this_tech': this_tech}
    return render(request, 'StoreApp/detail.html',context)

def orders(request):
    context = {}
    return render(request, 'StoreApp/orders.html',context)

def cart(request):
    context = {}
    return render(request, 'StoreApp/cart.html',context)

def checkout(request):
    context = {}
    return render(request, 'StoreApp/checkout.html',context)

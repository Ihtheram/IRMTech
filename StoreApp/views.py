from django.shortcuts import render

def store(request):
    context = {}
    return render(request, 'StoreApp/store.html',context)

def detail(request):
    context = {}
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

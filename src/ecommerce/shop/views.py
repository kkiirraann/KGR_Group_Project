from django.shortcuts import render
from .models import Category, Product, Contact
from math import ceil
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required


def home(request):
  allProds = []
  catprods = Product.objects.values('category', 'id')
  cats = {item['category'] for item in catprods}
  for cat in cats:
    prod = Product.objects.filter(category=cat)
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(1, nSlides), nSlides])
    if request.method == 'POST':
      params ={
        'allProds':allProds,
        'LogInText' : 'LogOut'
      }
    else:
      params ={
        'allProds':allProds,
        'LogInText' : 'LogIn'
      }
    return render(request, 'shop/home.html', params)


def about(request):
  return render(request,'shop/about.html')

# @login_url
def contact(request):
  if request.method=="POST":
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    message = request.POST.get('message', '')
    contact = Contact(name=name, email=email, phone=phone, message=message)
    contact.save()
  return render(request, 'shop/contact.html')

def account(request):
  return render(request,'shop/account.html')

def productview(request, myid):
  #fetch products by id
  product = Product.objects.filter(id=myid)
  print(product)
  return render(request,'shop/productview.html',{'product':product[0]})
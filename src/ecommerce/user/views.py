from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from .models import Users
from math import ceil
from shop.models import Category, Product, Contact
# Create your views here.

# def new_register(request):
#   if request.method == "POST":
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       username = form.cleaned_data.get('username')
#       messages.success(request,f'Account created for {username}!')
#       return redirect('shop/home.html')
#   else:
#     form = UserCreationForm()
#   return render(request,'user/new_register.html', {'form':form})


def index(request):
  if request.method == 'POST':
    context = {
      'email' : request.POST.get(email)
    }
  else:
    context = {
      'email' : ''
    }
  return render(request, 'user/index.html',context)

def login(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username,password=password)

    if user is not None:
      allProds = []
      catprods = Product.objects.values('category', 'id')
      cats = {item['category'] for item in catprods}
      for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        params = {
          'allProds':allProds,
          'user':user
        }
        return render(request, 'shop/home.html', params)
    else:
      context = {
            'message' : "User Does not Exists!",
            'username' : user.username
        }
      return render(request,'user/index.html', context)
  else:
    return render(request,'user/index.html')
      # print("Anonymous")
#     try:
#       user_details = User.objects.get(email = email)
#     except:
#       user_details = False
#     if email and password:
#       if user_details:
#         if user_details.password == password:
#           context ={
#             'email' : email
#           }
#           # shop.home(request,context)
#           return HttpResponseRedirect(reverse('shop-loggedIn-home',context=context))
#           # return redirect('shop-loggedIn-home', email=email)
#         else:
#           context = {
#             'message' : "Invalid Credentials",
#             'email' : email
#           }
#           return render(request,'user/index.html', context)
#       else:
#         context = {
#             'message' : "User Does not Exists!",
#             'email' : email
#         }
#         return render(request,'user/index.html', context)
#     else:
#       context = {
#         'message' : "Please fill in both email and password"
#       }  
#       return render(request,'user/index.html',context)


    

def register(request):
  #form = UserCreationForm()
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')
    try:
      already_exists = Users.objects.get(email_id = email)
    except:
      already_exists = False
    if password != confirm:
      context = {
        'P_message' : "Password doesn't match with confirmation"
      }
      return render(request, 'user/register.html',context)
    elif already_exists:
      context = {
        'A_message' : "User already Exists"
      }
      return render(request, 'user/register.html', context)
    else:
      save_user = Users(name=name, email_id=email, password=password, status=True, date_created=timezone.now()).save()
      context = {
        'message' : f'Account for { email } is successfully registered',
        'email' : email
      }
      return render(request,'user/index.html', context)
  else:
    # context = {
    #   'date1' : timezone.now
    # }
    return render(request, 'user/register.html')
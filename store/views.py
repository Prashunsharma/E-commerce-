from django.shortcuts import render,redirect
from . models import Product
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def home(request):
    products= Product.objects.all()
    return render(request, 'home.html',{'products': products})

def about(request):
     return render(request, 'about.html',{})

def login_(request):
     if request.method=="POST":
         username=request.POST['username']
         password=request.POST['password']
         user=authenticate(request,username=username,password=password)
         if user is not None:
              login(request,user)
              messages.success(request,(f"You have been logged  in sucessfully {username} "))
              return redirect('home')
         else :
               messages.success(request,("There was an error try again ..."))
               return redirect('login')
     else : 
            
         return render(request,'login.html',{})

def logout_(request):
     logout(request)
     messages.success(request,("You have been logged out... "))
     return redirect('home')

def register_(request):
     form =SignUpForm()
     if request.method=="POST":
          form=SignUpForm(request.POST)
          if form.is_valid():
               form.save()
               username=form.cleaned_data['username']
               password=form.cleaned_data['password1']
               user=authenticate(username=username,password=password)
               login(request,user)
               messages.success(request,(f"You are registered {username} Welcome..."))
               return redirect('home')
          else :
               messages.success(request,("There is some problem ..."))
               return redirect('register')
     else :          
        return render(request, 'register.html',{'form':form})
     

def product_(request,pk):
    product= Product.objects.get(id=pk)
    return render(request, 'product.html',{'product': product})
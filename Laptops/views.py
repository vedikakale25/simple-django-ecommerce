from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import LaptopModelForm
from .models import Laptops


# Create your views here.

#---------------Home Page view------------------
@login_required()
def home_view(request):
    qs=Laptops.objects.all()
    template_name='Laptops/home.html'
    context={"laptop":qs}
    return render(request, template_name, context)

#---------------Add Laptops Page view------------------
@login_required()
def add_view(request):
    form = LaptopModelForm()
    if request.method=="POST":
        form=LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect("/lapkart/show/")
    template_name='Laptops/add.html'
    context={"form":form}
    return render(request, template_name, context)

#---------------New User Registration Page view------------------
def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/auth/login/")
    template_name='Laptops/register.html'
    context={"form": form}
    return render(request, template_name, context)

#---------------Update Laptops Detail Page view------------------
@login_required()
def update_view(request,i):
    lap_obj=Laptops.objects.get(id=i)
    form=LaptopModelForm(instance=lap_obj)
    if request.method=="POST":
        form=LaptopModelForm(request.POST,instance=lap_obj)
        if form.is_valid():
            form.save()
            return redirect("/lapkart/show/")
    template_name='Laptops/register.html'
    context={"form":form}
    return render(request, template_name, context)

#---------------Delete Laptops Detail view------------------
@login_required()
def delete_view(request,i):
    lap_obj = Laptops.objects.get(id=i)
    lap_obj.delete()
    return redirect("/lapkart/show/")

#---------------Login Page view------------------
def login_view(request):
    if request.method=="POST":
        u=request.POST["uname"]
        p=request.POST["pw"]
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect("/lapkart/show/")
        else:
            messages.error(request,"Invalid Credentials")
    template_name = 'Laptops/login.html'
    context = {}
    return render(request, template_name, context)

#---------------Logout view------------------
def logout_view(request):
    logout(request)
    return redirect("/auth/login/")










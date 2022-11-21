import datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in
from django.contrib.auth import logout as log_out
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Crutch

# Create your views here.
def login(request):
    loginForm = AuthenticationForm()
    data = { "form": loginForm }
    return render(request, "login.html", context=data)

def authorize(request):
    if request.user.is_authenticated:
        return redirect("adminPanel/")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            log_in(request, user)
            return redirect("adminPanel/")
    return redirect('/login')

def logout(request):
    log_out(request)
    return redirect('/')

@login_required(login_url='/login')
def createCrutch(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        price = request.POST.get("price", None)
        description = request.POST.get("description", None)
        image = request.FILES.get("image", None)

        crutch = Crutch.objects.create(name=name, price=price, description=description, imageField=image, datePublished=datetime.datetime.now())
        return redirect(f"/crutch/{crutch.id}")
    
    return redirect('/adminPanel')

@login_required(login_url='/login')
def admin(request):
    allCrutches = Crutch.objects.all()
    data = { "crutches": allCrutches }
    return render(request, "admin.html", context=data)

@login_required(login_url='/login')
def editCrutch(request, id):
    try:
        if request.method == "POST":
            crutch = Crutch.objects.get(id=id)

            name = request.POST.get("name", None)
            price = request.POST.get("price", None)
            description = request.POST.get("description", None)
            image = request.FILES.get("image", None)

            if name is not None: crutch.name = name
            if price is not None: crutch.price = price
            if description is not None: crutch.description = description
            if image is not None: crutch.imageField = image

            crutch.save()
            return redirect(f"/crutch/{id}")
    except:
        return HttpResponseNotFound("Crutch not found!")

    try:
        crutch = Crutch.objects.get(id=id)
    except:
        return HttpResponseNotFound("Crutch not found!")
    
    data = { "crutch": crutch }
    return render(request, "edit.html", context=data)

@login_required(login_url='/login')
def delete(request, id):
    try:
        crutch = Crutch.objects.get(id=id)
        crutch.delete()
        return redirect('/adminPanel')
    except:
        return HttpResponseNotFound("Crutch not found!")
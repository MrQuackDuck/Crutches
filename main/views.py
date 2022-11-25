from django.http import HttpRequest
from django.shortcuts import render
from base64 import b64encode
from .models import Crutch
import json
import requests

def index(request):
    latestCrutches = Crutch.objects.all().order_by('-id')[:3]

    currentUahRate = getCurrentMoneyExchangeRate()

    for crutch in latestCrutches:
        crutch.uahPrice = round(int(crutch.price) * currentUahRate)
        if len(crutch.name) > 30:
            crutch.name = crutch.name[:30] + '...'
        if len(crutch.description) > 100:
            crutch.description = crutch.description[:100] + '...'

    data = { "crutches": latestCrutches }
    return render(request, "index.html", context=data)

def aboutUs(request):
    return render(request, "aboutUs.html")

def allCrutches(request):
    allCrutches = Crutch.objects.all()

    currentUahRate = getCurrentMoneyExchangeRate()

    for crutch in allCrutches:
        crutch.uahPrice = round(int(crutch.price) * currentUahRate)
        if len(crutch.name) > 30:
            crutch.name = crutch.name[:30] + '...'
        if len(crutch.description) > 100:
            crutch.description = crutch.description[:100] + '...'
    
    data = { "crutches": allCrutches }
    return render(request, "allCrutches.html", context=data)

def search(request):
    if request.method == "POST":
        searchString = request.POST.get("searchString")

        result = Crutch.objects.filter(name__in=searchString)
        print(result)

        data = { "crutches": result }
        return render(request, "allCrutches.html", context=data)

def crutch(request, id):
    currentUahRate = getCurrentMoneyExchangeRate()

    crutch = Crutch.objects.get(id=id)
    crutch.uahPrice = round(int(crutch.price) * currentUahRate)
    data = { "crutch": crutch }
    return render(request, "crutch.html", context=data)

def getCurrentMoneyExchangeRate():
    try:
        moneyExchangeApiUrl = 'https://api.exchangerate.host/convert?from=USD&to=UAH'
        response = requests.get(moneyExchangeApiUrl)
        currentUahRate = json.loads(response.text)["info"]["rate"]
    except:
        currentUahRate = 40
    return currentUahRate
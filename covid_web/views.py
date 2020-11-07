from django.http import HttpResponse
from django.shortcuts import render

from covid_web.covid_data import CountryCovidData, WorldCovidData
from covid_web.models import UserInfo


def index(request):
    cd = WorldCovidData()
    context = {
        'totalconfirm': cd.get_result("cases"),
        'newconfirm': cd.get_result("todayCases"),
        'totaldeaths': cd.get_result("deaths"),
        'newdeaths': cd.get_result("todayDeaths")
    }
    return render(request, 'index.html', context=context)

def details(request):
    cd = CountryCovidData()
    country = ""
    context = {
        'totalconfirm': cd.get_result("cases", country),
        'newconfirm': cd.get_result("todayCases", country),
        'totaldeaths': cd.get_result("deaths", country),
        'newdeaths': cd.get_result("todayDeaths", country),
        'totalconfirm': cd.get_result("", country),
        'newconfirm': cd.get_result("todayCases", country),
        'totaldeaths': cd.get_result("deaths", country),
        'newdeaths': cd.get_result("todayDeaths", country)
    }
    return render(request, 'index.html', context=context)


def detail(request):
    username = UserInfo.objects.all()
    context = {
        'username': username
    }
    return render(request, 'detail.html', context=context)


def register(request):
    return render(request, 'register.html')

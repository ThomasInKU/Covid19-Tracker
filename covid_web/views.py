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
    country_name = cd.country.keys()
    country = ""
    context = {
        'totalconfirm': cd.get_result("cases", country),
        'newconfirm': cd.get_result("todayCases", country),
        'totaldeaths': cd.get_result("deaths", country),
        'newdeaths': cd.get_result("todayDeaths",country),
        'recovered': cd.get_result("recovered", country),
        'todayRecovered': cd.get_result("todayRecovered", country),
        'active': cd.get_result("active", country),
    }
    
    return HttpResponse(request, 'details.html', context=context, country_name=country_name)


def detail(request):
    username = UserInfo.objects.all()
    context = {
        'username': username
    }
    return render(request, 'detail.html', context=context)


def register(request):
    return render(request, 'register.html')

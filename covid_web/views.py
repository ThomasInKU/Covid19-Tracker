from django.http import HttpResponse
from django.shortcuts import render

from covid_web.covid_data import CountryCovidData, WorldCovidData
from covid_web.models import UserInfo


def index(request):
    cd = WorldCovidData()
    context = {
        'totalconfirm': "{:,}".format(cd.get_result("cases")),
        'newconfirm': "{:,}".format(cd.get_result("todayCases")),
        'totaldeaths': "{:,}".format(cd.get_result("deaths")),
        'newdeaths': "{:,}".format(cd.get_result("todayDeaths"))
    }
    return render(request, 'index.html', context=context)

def details(request):
    cd = CountryCovidData()
    country = str(request.GET.get('country', ''))
    context = {
        'name' : country,
        'country_name' : list(cd.country.keys()),
        'totalconfirm': "{:,}".format(cd.get_result("cases", country)),
        'newconfirm': "{:,}".format(cd.get_result("todayCases", country)),
        'totaldeaths': "{:,}".format(cd.get_result("deaths", country)),
        'newdeaths': "{:,}".format(cd.get_result("todayDeaths",country)),
        'recovered': "{:,}".format(cd.get_result("recovered", country)),
        'todayRecovered': "{:,}".format(cd.get_result("todayRecovered", country)),
        'active': "{:,}".format(cd.get_result("active", country)),
    }
    
    return render(request, 'details.html', context=context)


def detail(request):
    username = UserInfo.objects.all()
    context = {
        'username': username
    }
    return render(request, 'detail.html', context=context)


def register(request):
    return render(request, 'register.html')

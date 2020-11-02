from django.http import HttpResponse
from django.shortcuts import render

from covid_web.covid_data import CovidData
from covid_web.models import UserInfo


def index(request):
    cd = CovidData()
    context = {
        'totalconfirm': cd.today_total_data("cases"),
        'newconfirm': cd.today_total_data("todayCases"),
        'totaldeaths': cd.today_total_data("deaths"),
        'newdeaths': cd.today_total_data("todayDeaths")
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

from django.http import HttpResponse
from django.shortcuts import render

from covid_web.covid_data import CovidData
from covid_web.models import UserInfo


def index(request):
    cd = CovidData()
    context = {
        'totalconfirm': cd.today_total_confirm_data("World","totalconfirm"),
        'newconfirm': cd.today_total_confirm_data("World","newconfirm"),
        'totaldeaths': cd.today_total_confirm_data("World","totaldeaths"),
        'newdeaths': cd.today_total_confirm_data("World","newdeaths")
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

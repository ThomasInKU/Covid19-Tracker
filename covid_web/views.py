from django.http import HttpResponse
from django.shortcuts import render

from covid_web.models import UserInfo


def index(request):
    username = UserInfo.objects.all()
    context = {
        'username': username
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

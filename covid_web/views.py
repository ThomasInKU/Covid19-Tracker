from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from covid_web.covid_data import CovidData
from covid_web.forms import SignUpForm


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


def signup(request):
    """Register a new user."""

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_passwd , email = email)
            login(request, user)
            return redirect('index')
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

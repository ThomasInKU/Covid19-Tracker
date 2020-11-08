from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from covid_web.covid_data import CovidData
from covid_web.forms import SignUpForm
from django.contrib.auth import views as auth_views


class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "Incorrect username or password"
        ),
        'inactive': ("This account is inactive."),
    }

class MyLoginView(auth_views.LoginView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        cd = CovidData()
        form = MyAuthForm(data=self.request.POST or None)
        context = {
            'form': form,
            'totalconfirm': cd.today_total_data("cases"),
            'newconfirm': cd.today_total_data("todayCases"),
            'totaldeaths': cd.today_total_data("deaths"),
            'newdeaths': cd.today_total_data("todayDeaths")
        }
        return context


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
    context = {
        'username': ""
    }
    return render(request, 'detail.html', context=context)


def register(request):
    return render(request, 'register.html')


def signup(request):
    """Register a new user."""

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

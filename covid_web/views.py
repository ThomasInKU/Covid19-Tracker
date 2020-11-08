from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from covid_web.covid_data import CountryCovidData, WorldCovidData
from covid_web.forms import SignUpForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

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
        cd = WorldCovidData()
        form = MyAuthForm(data=self.request.POST or None)
        context = {
            'form': form,
            'totalconfirm': "{:,}".format(cd.get_result("cases")),
            'newconfirm': "{:,}".format(cd.get_result("todayCases")),
            'totaldeaths': "{:,}".format(cd.get_result("deaths")),
            'newdeaths': "{:,}".format(cd.get_result("todayDeaths"))
        }
        return context

def my_logout(request):
     return auth_views.logout(request)

def index(request):
    cd = WorldCovidData()
    context = {
        'totalconfirm': "{:,}".format(cd.get_result("cases")),
        'newconfirm': "{:,}".format(cd.get_result("todayCases")),
        'totaldeaths': "{:,}".format(cd.get_result("deaths")),
        'newdeaths': "{:,}".format(cd.get_result("todayDeaths"))
    }
    return render(request, 'index.html', context=context)

@login_required()
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

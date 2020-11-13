from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from covid_web.covid_data import CountryCovidData, WorldCovidData
from covid_web.forms import SignUpForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


class MyAuthForm(AuthenticationForm):
    """Class that contains error message for invalid login."""
    error_messages = {
        'invalid_login': (
            "Incorrect username or password"
        ),
        'inactive': ("This account is inactive."),
    }


class MyLoginView(auth_views.LoginView):
    """Class that contains configuration for index page."""
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


@login_required()
def details(request):
    """Get data from user and show data from that country"""
    cd = CountryCovidData()
    country = str(request.GET.get('country', ''))
    if country != '':
        context = {
            'name': country,
            'country_name': list(cd.country.keys()),
            'totalconfirm': "{:,}".format(cd.get_result("cases", country)),
            'newconfirm': "{:,}".format(cd.get_result("todayCases", country)),
            'totaldeaths': "{:,}".format(cd.get_result("deaths", country)),
            'newdeaths': "{:,}".format(cd.get_result("todayDeaths", country)),
            'recovered': "{:,}".format(cd.get_result("recovered", country)),
            'todayRecovered': "{:,}".format(cd.get_result("todayRecovered", country)),
            'active': "{:,}".format(cd.get_result("active", country)),
        }
    else:
        context = {
            'name': country,
            'country_name': list(cd.country.keys()),
            'totalconfirm': cd.get_result("cases", country),
            'newconfirm': cd.get_result("todayCases", country),
            'totaldeaths': cd.get_result("deaths", country),
            'newdeaths': cd.get_result("todayDeaths", country),
            'recovered': cd.get_result("recovered", country),
            'todayRecovered': cd.get_result("todayRecovered", country),
            'active': cd.get_result("active", country),
        }
        
    return render(request, 'details.html', context=context)


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
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

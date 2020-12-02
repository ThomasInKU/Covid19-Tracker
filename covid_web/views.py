"""The view configuration for covid-web app."""
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from covid_web.covid_data import CountryCovidData, WorldCovidData, ThailandCovidData
from covid_web.forms import SignUpForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
import requests
from covid_web.sheets import Sheet


class MyAuthForm(AuthenticationForm):
    """Class that contains error message for invalid login."""

    error_messages = {
        'invalid_login': (
            "Incorrect username or password"
        ),
        'inactive': "This account is inactive.",
    }


class MyLoginView(auth_views.LoginView):
    """Class that contains configuration for index page."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Get covid data and show in index page."""
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


class User_info:
    """Class for initialize values of detail page"""

    def __init__(self):
        self.user_ip = ""
        self.user_country = ""
        self.user_lattitude = ""
        self.user_longtitude = ""
        self.sheet = ""
        self.pinned = ""


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_location_form_ip(ip):
    url = f"http://api.ipstack.com/{ip}?access_key={'99c3ea4ed446e04a08202b66f6970772'}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# def get_user_ip(request):
#     res = requests.get('https://ipinfo.io/')
#     data = res.json()
#     ip = data['ip']
#     location = data['loc'].split(',')
#     latti = location[0]
#     longti = location[1]
#     return ip, latti, longti


def get_address_from_country(country):
    pass


cd = CountryCovidData()
uf = User_info()


@login_required()
def details(request):
    """Get data from user and show data from that country."""
    country = str(request.GET.get('country', ''))
    error_warning = False
    if country not in list(cd.country.keys()) and country != "":
        error_warning = True
    if country == "":
        # first load of the web page
        uf.user_ip, uf.user_lattitude, = get_client_ip(request)
        uf.user_lattitude = get_location_form_ip()["latitude"]
        uf.user_longtitude = get_location_form_ip()["longitude"]
        uf.user_country = get_location_form_ip(uf.user_ip)["country_name"]
        country = uf.user_country
        uf.sheet = Sheet(request.user.username)
        uf.pinned = uf.sheet.call_countries()
    if request.method == 'POST' and 'add_country' in request.POST:
        uf.sheet.add_country(country)
        uf.pinned = uf.sheet.call_countries()
    if request.method == 'GET' and 'delete_country' in request.GET:
        area = request.GET.get('area', '')
        uf.sheet.delete_cell(area)
        uf.pinned = uf.sheet.call_countries()
    if request.method == 'GET' and 'jump' in request.GET:
        country = request.GET.get('area', '')
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
        'error_warning': error_warning,
        'user_country': uf.user_country,
        'user_lattitude': uf.user_lattitude,
        'user_longtitude': uf.user_longtitude,
        'ip': uf.user_ip,
        'pinnedarea': uf.pinned,
    }
    return render(request, 'details.html', context=context)


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
        # what if form is not valid?
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def prevent(request):
    """Render prevent page."""
    context = {}
    return render(request, 'prevent.html', context=context)


td = ThailandCovidData()

@login_required()
def map(request):
    """Render prevent page."""
    province = str(request.GET.get('province', ''))
    context = {'totalconfirm': "{:,}".format(td.get_result(province)),
               'province': province,
               'location' : uf.user_country,
               'ip': uf.user_ip}
    return render(request, 'th_map.html', context=context)

from django.urls import path

from . import views

urlpatterns = [
    path('', views.MyLoginView.as_view(), name="index"),
    path('signup/', views.signup, name='signup'),
    path('country/', views.details, name='details'),
    path('logout/',views.my_logout, name='logout')
]
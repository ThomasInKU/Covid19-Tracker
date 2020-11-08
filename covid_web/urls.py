from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('', views.MyLoginView.as_view(), name="index"),
]
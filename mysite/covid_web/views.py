"""import."""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
from django.contrib import messages

# Create your views here.

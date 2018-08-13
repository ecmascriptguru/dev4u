from django.shortcuts import render
from .models import Organization
from django.http import HttpResponse

# Create your views here.
def index():
    # return HttpResponse("Hello, world. You're at the polls index.")
    return "Hello, this is organization view"
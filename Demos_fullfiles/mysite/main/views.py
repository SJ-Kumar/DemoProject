from mysite.main.models import Tutorial
from django.shortcuts import render
from django.http import HttpResponse

def homepage (request):
    return HttpResponse("Wow this is response from <strong>views</strong> page!")

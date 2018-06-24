from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404


def index(request):
    return render(request, 'contact/contact.html')

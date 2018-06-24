from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import reg



def index(request):
    all_reg = reg.objects.all().order_by('-date')
    return render(request, 'register/register.html',{'all_reg':all_reg})


def detail_reg(request,reg_id):
    temp = reg.objects.get(pk=reg_id)
    return render(request, 'register/showInfo.html',{'reg':temp})

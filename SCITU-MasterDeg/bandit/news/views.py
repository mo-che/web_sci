from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import public,fund



def news_public(request):
    all_public = public.objects.all().order_by('-date')
    return render(request, 'news/news_public.html',{'all_public':all_public})

def news_fund(request):
    all_fund = fund.objects.all().order_by('-date')
    return render(request, 'news/news_fund.html',{'all_fund':all_fund})


def detail_public(request,public_id):
    news = public.objects.get(pk=public_id)
    return render(request, 'news/showInfo.html',{'news':news})

def detail_fund(request,fund_id):
    news = fund.objects.get(pk=fund_id)
    return render(request, 'news/showInfo.html',{'news':news})

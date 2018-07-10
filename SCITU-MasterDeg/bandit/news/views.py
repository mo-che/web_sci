from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import public,fund
from .forms import PublicForm,FundForm
from django.shortcuts import redirect


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

def public_upload(request):
    if request.method == 'POST':
        form = PublicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/news/public')
    else:
        form = PublicForm()
    return render(request, 'news/uploadfile.html', {
        'form': form
    })

def fund_upload(request):
    if request.method == 'POST':
        form = FundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/news/fund')
    else:
        form = FundForm()
    return render(request, 'news/uploadfile.html', {
        'form': form
    })

def public_delete(request,id):
   #+some code to check if New belongs to logged in user
   u = public.objects.get(pk=id).delete()
   return HttpResponseRedirect("/news/public")

def fund_delete(request,id):
   #+some code to check if New belongs to logged in user
   u = fund.objects.get(pk=id).delete()
   return HttpResponseRedirect("/news/fund")
   
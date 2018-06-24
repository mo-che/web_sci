from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from . models import form,document,EngDocument


def index(request):
    all_form = form.objects.all()
    all_document = document.objects.all()
    all_EngDocument = EngDocument.objects.all()
    return render(request, 'documents/documents.html',{'all_form':all_form,  'all_document':all_document , 'all_EngDocument':all_EngDocument})

def detail_form(request,form_id):
    forms = form.objects.get(pk=form_id)
    return render(request, 'documents/detail.html',{'form':forms})

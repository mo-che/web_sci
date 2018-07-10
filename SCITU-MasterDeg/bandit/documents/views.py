from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from . models import form,document,EngDocument
from .forms import DocumentForm,formForm,EngDocForm
from django.shortcuts import redirect

def index(request):
    all_form = form.objects.all()
    all_document = document.objects.all()
    all_EngDocument = EngDocument.objects.all()
    return render(request, 'documents/documents.html',{'all_form':all_form,  'all_document':all_document , 'all_EngDocument':all_EngDocument})

def detail_form(request,form_id):
    forms = form.objects.get(pk=form_id)
    return render(request, 'documents/detail.html',{'form':forms})


def model_document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/documents')
    else:
        form = DocumentForm()
    return render(request, 'documents/uploadfile.html', {
        'form': form
    })

def model_form_upload(request):
    if request.method == 'POST':
        form = formForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/documents')
    else:
        form = formForm()
    return render(request, 'documents/uploadfile.html', {
        'form': form
    })

def model_EngDocument_upload(request):
    if request.method == 'POST':
        form = EngDocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/documents')
    else:
        form = EngDocForm()
    return render(request, 'documents/uploadfile.html', {
        'form': form
    })

def document_delete(request,id):
   #+some code to check if New belongs to logged in user
   u = document.objects.get(pk=id).delete()
   return HttpResponseRedirect("/documents")

def form_delete(request,id):
   #+some code to check if New belongs to logged in user
   u = form.objects.get(pk=id).delete()
   return HttpResponseRedirect("/documents")

def engDoc_delete(request,id):
   #+some code to check if New belongs to logged in user
   u = EngDocument.objects.get(pk=id).delete()
   return HttpResponseRedirect("/documents")
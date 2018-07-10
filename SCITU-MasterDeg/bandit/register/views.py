from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import reg
from .forms import RegisForm
from django.shortcuts import redirect


def index(request):
    all_reg = reg.objects.all().order_by('-date')
    return render(request, 'register/register.html',{'all_reg':all_reg})


def detail_reg(request,reg_id):
    temp = reg.objects.get(pk=reg_id)
    print(temp)
    return render(request, 'register/showInfo.html',{'reg':temp})

def reg_upload(request):
    if request.method == 'POST':
        form = RegisForm(request.POST, request.FILES)
        if form.is_valid():
            print("Pass")
            form.save()
            return redirect('/register')
    else:
        form = RegisForm()
    return render(request, 'register/uploadfile.html', {
        'form': form
    })

def reg_delete(request,reg_id):
   #+some code to check if New belongs to logged in user
   u = reg.objects.get(pk=reg_id).delete()
   return HttpResponseRedirect("/register") # wherever to go after deleting

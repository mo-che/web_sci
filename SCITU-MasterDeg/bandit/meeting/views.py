from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from . models import meetingTable,report
from .forms import MeetingForm,ReportForm
from django.shortcuts import redirect

def index(request):
    all_meetingTable = meetingTable.objects.all()
    all_report = report.objects.all()
    year_report = report.objects.all().datetimes('date','year')
    return render(request, 'meeting/meeting.html', {'all_meetingTable':all_meetingTable,'all_report':all_report,'year_report':year_report})

def meeting_upload(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/meeting')
    else:
        form = MeetingForm()
    return render(request, 'meeting/uploadfile.html', {
        'form': form
    })

def report_upload(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/meeting')
    else:
        form = ReportForm()
    return render(request, 'meeting/uploadfile.html', {
        'form': form
    })

def meet_delete(request,id):
   #+some code to check if New belongs to logged in user
   u = meetingTable.objects.get(pk=id).delete()
   return HttpResponseRedirect("/meeting")
   
def report_delete(request,id):
   #+some code to check if New belongs to logged in user
   u = report.objects.get(pk=id).delete()
   return HttpResponseRedirect("/meeting")
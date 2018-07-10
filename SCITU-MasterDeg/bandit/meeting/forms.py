from django import forms
from .models import meetingTable,report

class MeetingForm(forms.ModelForm):
    class Meta:
        model = meetingTable
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta:
        model = report
        fields = '__all__'
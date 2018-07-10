from django import forms
from .models import reg

class RegisForm(forms.ModelForm):
    class Meta:
        model = reg
        fields = '__all__'
        exclude = ['file']

from django import forms
from .models import public,fund

class PublicForm(forms.ModelForm):
    class Meta:
        model = public
        fields = '__all__'

class FundForm(forms.ModelForm):
    class Meta:
        model = fund
        fields = '__all__'
from django import forms
from .models import document,form,EngDocument

class DocumentForm(forms.ModelForm):
    class Meta:
        model = document
        fields = '__all__'

class formForm(forms.ModelForm):
    class Meta:
        model = form
        fields = '__all__'

class EngDocForm(forms.ModelForm):
    class Meta:
        model = EngDocument
        fields = '__all__'
from xml.parsers.expat import model
from django import forms
from .models import Publisher

class AddFormPublisher(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"



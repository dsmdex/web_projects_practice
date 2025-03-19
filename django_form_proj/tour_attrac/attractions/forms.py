from django import forms
from .models import State, Attraction

class CreateStateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"

class CreateAttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = "__all__"
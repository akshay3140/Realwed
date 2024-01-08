from vender.models import coupledetail
from django import forms
from django.db import models
from django.forms import fields
from app.models import *

class coupled(forms.ModelForm):
    class Meta:
        model=coupledetail
        fields='__all__'
class venueform(forms.ModelForm):
    class Meta:
        model=venuedetail
        fields='__all__'
class photographerform(forms.ModelForm):
    class Meta:
        model=photographerdetail
        fields='__all__'
class caterersform(forms.ModelForm):
    class Meta:
        model=cakedetail
        fields='__all__'
class beauticionform(forms.ModelForm):
    class Meta:
        model=beautisiondetail
        fields='__all__'
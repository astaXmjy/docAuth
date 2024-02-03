from django import forms

from .models import Aadhar


class AadharForm(forms.ModelForm):

    class Meta:
        model=Aadhar
        fields=['image']
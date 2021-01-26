from django import forms 
from .models import home


class GeeksForm(forms.ModelForm):
    class Meta:
        model = home
        fields = ["geeks_field"]



from django import forms
from .models import Donor


class DonorForm(forms.ModelForm):
    class Meta:

        model = Donor
        firstname = forms.CharField(label='name',
                                    widget=forms.TextInput(attrs={'placeholder': 'name'}))
        fields = '__all__'

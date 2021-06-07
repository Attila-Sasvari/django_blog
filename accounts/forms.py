from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=settings.YEAR_CHOICES, attrs={'class': 'form-control, m-2', }))

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }
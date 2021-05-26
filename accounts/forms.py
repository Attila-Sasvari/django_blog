from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=settings.YEAR_CHOICES))

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')
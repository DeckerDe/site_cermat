from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Profile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'photo')




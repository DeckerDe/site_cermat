from django.contrib.auth import get_user_model, forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from django.conf import settings
from allauth.account.adapter import get_adapter
from allauth.account import app_settings
import pdb

User = get_user_model()


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "name", "photo", "researchgate", "linkedin", "lattes"
        ]


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(SignupForm):

    def clean_email(self):
        value = self.cleaned_data["email"]
        value = get_adapter().clean_email(value)
        if value and app_settings.UNIQUE_EMAIL:
            value = self.validate_unique_email(value)
            if value.split("@")[1] not in settings.ALLOWED_MAIL:
                raise ValidationError("Apenas Emails da UFSC são válidos.")
        return value

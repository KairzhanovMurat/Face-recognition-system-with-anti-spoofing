from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True, label='Your Email')
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),

    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."))

    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'face_image')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "password1", "password2"]


#############################################################################3
class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = get_user_model()
        fields = ["email"]


###############################################################################
class CustomSetPasswordForm(SetPasswordForm):
    class Meta:
        widgets = {
            "new_password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "new_password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

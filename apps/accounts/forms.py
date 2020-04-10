from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',
                                   widget=forms.PasswordInput(
                                       attrs={
                                           "class": "form-control"
                                       }
                                   ))
    new_password1 = forms.CharField(label='New Password',
                                    widget=forms.PasswordInput(
                                        attrs={
                                            "class": "form-control"
                                        }
                                    ))
    new_password2 = forms.CharField(label='Confirm New Password',
                                    widget=forms.PasswordInput(
                                        attrs={
                                            "class": "form-control"
                                        }
                                    ))

    # def clean_old_pwd(self, *args, **kwargs):
    #     pass

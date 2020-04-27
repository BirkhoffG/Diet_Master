from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm


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

    # def clean_new_password1(self):
    #     password_1 = self.cleaned_data.get('new_password1')
    #     if len(password_1) > 18 or len(password_1) < 7:
    #         raise forms.ValidationError("The password should be at least 8 characters")
    #     elif password_1.isdigit():
    #         raise forms.ValidationError("The password can't be entirely numeric.")
    #     return password_1


class ChangeEmailForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email address"
        }
    ))




class SurveyForm(forms.Form):

    YEARS = [x for x in range(1960, 2020)]

    weight = forms.DecimalField(max_value=200, min_value=0, decimal_places=1)
    height = forms.DecimalField(max_value=250, min_value=0, decimal_places=1)
    target_weight = forms.DecimalField(max_value=200, min_value=0, decimal_places=1)
    gender = forms.ChoiceField(widget=forms.RadioSelect, initial='male',
                               choices=(('male', 'male'), ('female', 'female')))


    birth_date = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
    duration = forms.IntegerField(max_value=180, min_value=15)
    activity_level = forms.ChoiceField(widget=forms.RadioSelect, initial=1.1,
                                       choices=((1.1, '1.1'), (1.2, '1.2'), (1.3, '1.3'), (1.4, '1.4')))


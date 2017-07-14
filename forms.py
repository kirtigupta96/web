from .models import Education
from .models import Company
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from verified_email_field.forms import VerifiedEmailField







#   FOR APPLICANT PROFILE
class SignUpForm(UserCreationForm):
    Options = (('0', 'Applicant'),
               ('1', 'Company'),)
    first_name = forms.ChoiceField(choices=Options, required=True)
    #last_name = forms.BooleanField(required=True)

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2', )
        labels = {
            'first_name': "Sign up as",
        }


# For Company Profile
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'about', 'website',)


CATEGORIES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )


class SecondaryEducationForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=CATEGORIES, required=True)

    class Meta:
        model = Education
        fields = ('name', 'homeadd', 'dob', 'contact','gender', 'yoc1', 'board1', 'percentage1', 'yoc2', 'board2', 'percentage2',
                  'yoc3', 'percentage3','college','course',
                  'company_i', 'duration', 'profile_i', 'company_i2', 'duration2', 'profile_i2',
                  'title_p','description_p','skills', 'work', 'git_hub', 'linked_in',)


class SearchForm(forms.Form):
    search= forms.CharField(label="Search by post",max_length=250,widget=forms.TextInput(attrs={'placeholder': 'Enter the interns post required'}))


class PasswordForm(forms.Form):
    email1 = forms.CharField(label="Email id",max_length=250,widget=forms.TextInput(attrs={'placeholder': 'E-mail id for receiving password'}))



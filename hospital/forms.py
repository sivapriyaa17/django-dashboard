from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
class Signup(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm password",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','profile','username','email','type','password1','password2','address','city','state','pincode']
        def clean(self):
            cleaned_data=super().clean()
            password1=cleaned_data.get("password1")
            password2=cleaned_data.get("password2")
            if password1 and password2 and password1!=password2:
                raise forms.ValidationError("passwords do not match")
            return cleaned_data

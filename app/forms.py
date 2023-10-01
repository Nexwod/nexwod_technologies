from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm

from django.contrib.auth.models import User
from .models import Customer

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus" : "True",
    "class":"form-control" }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    "autocomplete":"current-password", "class":"form-control"}))



class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus" : "True",
    "class":"form-control" }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
    "class":"form-control" }))
    password1 = forms.CharField( label= 'Password', widget=forms.PasswordInput(attrs={
    "class":"form-control"}))
    password2 = forms.CharField( label= 'Confirm Password', widget=forms.PasswordInput(attrs={
    "class":"form-control" }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MyPasswordResetForm(PasswordChangeForm):
    pass



class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label = 'Old Password', widget=forms.PasswordInput(attrs={'autofocus': 'True', 
    'autocomplete':'current-password', 'class': 'form-control'}))
    new_password1 = forms.CharField(label = 'New Password', widget=forms.PasswordInput(attrs={
    'autocomplete':'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput(attrs={
    'autocomplete':'current-password', 'class': 'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'name', 'address','locality', 'city', 'mobile', 'email','state' ]
        widgets = {
            'name': forms.TextInput(attrs={"autofocus" : "True","class":"form-control" }),
            'address': forms.TextInput(attrs={"autofocus" : "True","class":"form-control" }),
            'locality': forms.TextInput(attrs={"autofocus" : "True","class":"form-control" }),
            'city': forms.TextInput(attrs={"autofocus" : "True","class":"form-control" }),
            'mobile': forms.NumberInput(attrs={"autofocus" : "True","class":"form-control" }),
            'email': forms.TextInput(attrs={"autofocus" : "True","class":"form-control" }),
            'state': forms.Select(attrs={"autofocus" : "True","class":"form-control" }),
        }


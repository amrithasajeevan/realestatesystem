from django import forms
from  .models import *
from django .views import generic


class AdminRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = adminuser
        fields = '__all__'

class AdminLoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=15,widget=forms.PasswordInput)


class PropertyForm(forms.ModelForm):
    class Meta:
        model= propertydetail
        fields = '__all__'


class PropertyForm(forms.ModelForm):
    class Meta:
        model= propertydetail
        fields = '__all__'


class TenentRegForm(forms.ModelForm):
    class Meta:
        model=tenentreg
        fields='__all__'


class TenentLoginForm(forms.Form):
    name=forms.CharField(max_length=50)
    password=forms.CharField(max_length=15)

class TenantRequestForm(forms.ModelForm):
    class Meta:
        model = TenantRequest
        fields = ['tenant', 'property_interest', 'message']

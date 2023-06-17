from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #UserCreationForm od Adamsa
from django.shortcuts import redirect, render
from .models import Category, Transaction, User #usunięto Account
from django.contrib.auth import get_user_model

User = get_user_model()


class FormWithCaptcha(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

"""
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'login',
            'password',
        ]

        widgets = {
            "login": forms.TextInput(attrs={'placeholder': 'Wpisz nazwę kategorii', 'style': 'width:450px; height:80px'}),
            "password": forms.TextInput(attrs={'type': 'password','placeholder': 'Wpisz nazwę kategorii', 'style': 'width:450px; height:80px'}),

        }
"""

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',

        ]

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Wpisz nazwę kategorii', 'style': 'width:450px; height:80px'})

        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'expense_or_proceeds',
            'transaction',
            'category',
            'amount',
            'date_of_transaction'
        ]

        widgets = {
            "transaction": forms.TextInput(attrs={'placeholder': 'Podaj opis transakcji', 'style': 'width:450px; height:80px'}),
            "amount": forms.TextInput(attrs={'placeholder': 'Podaj należność transakcji', 'style': 'width:450px; height:80px'}),
            "date_of_transaction": forms.DateInput( attrs={'type':'date','placeholder': 'Podaj datę wykonania transakcji', 'style': 'width:450px; height:40px'}),

        }

"""
class register_form(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'login',
            'password',
            'email',
    ]

        widgets = {
            "login": forms.TextInput(attrs={'placeholder': 'Wpisz login', 'style': 'width:450px; height:80px'}),
            "password": forms.TextInput(attrs={'type': 'password', 'placeholder': 'Wpisz hasło', 'style': 'width:450px; height:80px'}),
            "email": forms.TextInput(attrs={'type': 'email', 'placeholder': 'Podaj e-mail', 'style': 'width:450px; height:80px'}),
    }
"""

#Kod Adamsa poniżej

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    
    email=forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

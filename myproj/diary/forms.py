#!/usr/bin/env python3
from django import forms
from .models import ActiveUser


class DailyForm(forms.Form):

    usr_data = [("taiseiyo", "taiseiyo"),
                ("syasin", "syasin")]

    # choice = forms.ChoiceField(label="user name", choices=usr_data)
    name = forms.CharField(label="name",
                           widget=forms.TextInput(
                               attrs={"class": "form-control"}))
    password = forms.CharField(label="password",
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control"}))


class RegisterForm(forms.Form):
    name = forms.CharField(label="name",
                           widget=forms.TextInput(
                               attrs={"class": "form-control"}))
    mail = forms.EmailField(label="email",
                            widget=forms.EmailInput(
                                attrs={"class": "form-control"}))


class Re_RegisterForm(forms.ModelForm):
    class Meta:
        model = ActiveUser
        fields = ["name", "mail"]


class RestrictForm(forms.Form):
    password = forms.CharField(label="password",
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control"}))

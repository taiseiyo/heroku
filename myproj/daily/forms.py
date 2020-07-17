from django import forms


class DailyForm(forms.Form):
    name = forms.CharField(label="name")
    password = forms.CharField(label="password")

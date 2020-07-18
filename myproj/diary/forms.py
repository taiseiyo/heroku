from django import forms


class DailyForm(forms.Form):
    name = forms.CharField(label="name",
                           widget=forms.TextInput(
                               attrs={"class": "form-control"}))

    password = forms.CharField(label="password",
                               widget=forms.TextInput(
                                   attrs={"class": "form-control"}))

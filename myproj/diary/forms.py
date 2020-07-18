from django import forms


class DailyForm(forms.Form):

    usr_data = [("one", "taiseiyo")]

    choice = forms.ChoiceField(label="user name", choices=usr_data)

    name = forms.CharField(label="name",
                           widget=forms.TextInput(
                               attrs={"class": "form-control"}))

    password = forms.CharField(label="password",
                               widget=forms.TextInput(
                                   attrs={"class": "form-control"}))

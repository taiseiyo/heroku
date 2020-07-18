from django import forms


class DailyForm(forms.Form):

    usr_data = ["one", "taisei"]
    choice = forms.MultipleChoiceField(label="usr", choices=usr_data,
                                       widget=forms.SelectMultiple(attrs={"size": 1}))
    name = forms.CharField(label="name",
                           widget=forms.TextInput(
                               attrs={"class": "form-control"}))

    password = forms.CharField(label="password",
                               widget=forms.TextInput(
                                   attrs={"class": "form-control"}))

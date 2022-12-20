from django import forms

class NewDiary(forms.Form):
    title = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Title"}
        )
    )
    content = forms.CharField(
        label ="",
        widget= forms.Textarea (
            attrs = {"class": "form-control form-control-lg", "placeholder": "Content"}
        ),
    )
    date = forms.DateTimeField(
        label ="",
        widget=forms.DateTimeInput(
            attrs={"class" : "form-control form-control-lg", "placeholder" : "time"}
        )
    )
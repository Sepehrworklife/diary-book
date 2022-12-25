from django import forms

class NewDiary(forms.Form):
    title = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={"style": "background-color: transparent; width:100%; border: 0; outline: 0;text-align: center; font-size: 2rem;padding: 10px 24px;", "placeholder": "Title"}
        )
    )
    content = forms.CharField(
        label ="",
        widget= forms.Textarea (
            attrs = {"placeholder": "Content", "id": "content", "class": "d-none"}
        ),
    )
    date = forms.DateTimeField(
        label ="",
        widget=forms.DateTimeInput(
            attrs={"style" : "background-color: transparent; border: 0; outline: 0; font-size: 1rem; padding: 10px 24px;", "placeholder" : "Time", "type": "date"}
        )
    )
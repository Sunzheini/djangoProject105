from django import forms


class PersonForm(forms.Form):
    your_name = forms.CharField(
        max_length=30,
        label='Ur name',
        help_text='Enter your name',
    )

    age = forms.IntegerField(
        required=False,
        label='Your age',
    )











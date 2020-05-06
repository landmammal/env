from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=256)
    nickname = forms.CharField(label='Nickname', max_length=256)
    age = forms.IntegerField(label='Age', min_value=18)

    

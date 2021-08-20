from django import forms
from django.contrib.auth.models import User

class RegistrateForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class':'control-label'}),
            'password2': forms.PasswordInput(attrs={'class':'control-label'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
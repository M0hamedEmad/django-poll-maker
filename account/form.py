from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserregisterionForm(UserCreationForm):
    # first_name= forms.CharField(max_length=100)
    # last_name= forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['password1'].help_text = ' '
        self.fields['password2'].help_text = ' '
        self.fields['username'].help_text = ' '
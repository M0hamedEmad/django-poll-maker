from django import forms
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        user = User.objects.get(username=username)
        
        if User.objects.filter(email=email).count() > 1:
            raise forms.ValidationError('Email already exists.')        
   
        return email  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


#register user

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','password1','password2']
        

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control'
        })
        
        # Remove labels if desired
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
       
    

#login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    # password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))



# - Create a record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'gender' ,'email', 'phone', 'address', 'city', 'province', 'country']

    def __init__(self, *args, **kwargs):
        super(CreateRecordForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': field_name.replace('_', '').title(),
                'class': 'form-control'
            })
            field.label = ''

            

                

#- Update a record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone', 'address', 'city', 'province', 'country']

    def __init__(self, *args, **kwargs):
        super(UpdateRecordForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': field_name.replace('_', '').title(),
                'class': 'form-control'
            })
            field.label = ''

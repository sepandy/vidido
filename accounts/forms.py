from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile
genders = [('male', 'male'), ('female' , 'female'), ('other', 'other') ,('alien', 'alien')]

class SignUpForm(UserCreationForm):

    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    bio = forms.Textarea()
    gender = forms.CharField(max_length=10,widget=forms.Select(choices=genders))



    class Meta:
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        model = User
        widgets = {
            'bio': forms.Textarea(attrs={
                'placeholder':'biography...',
            })
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user','friends']

        widgets = {
            'bio': forms.Textarea(attrs={
                'placeholder':'biography...',
            }),
            'birthday':forms.DateInput(attrs={
                'type': 'date'

            }),
            'gender':forms.Select(choices=genders),
            'profile_photo':forms.FileInput(attrs={
                'accept': 'image/*'
            })
        }
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = ['user',]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=1000, widget=forms.PasswordInput)

    class Meta:
        fields = '__all__'
        # model = User
from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.contrib.auth.models import User
from .models import Project, ProjectOwner, Investor, Analyst


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            return user

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


#Exemple de formulaire personnalise base sur AuthentificationForm
class custumerAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'owner']

class ProjectOwnerForm(forms.ModelForm):
    class Meta:
        model = ProjectOwner
        fields = ['user']

class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ['user']
        
class AnalystForm(forms.ModelForm):
    class Meta:
        model = Analyst
        fields = ['user']


        
from django import forms
from . models import ContactModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class ContactForm(forms.ModelForm):
    
    class Meta:
        
        model = ContactModel
        
        fields = ['fname','lname','contact','email','requirement']
        
        labels = {
            'fname':'First Name ',
            'lname':'Last Name ',
            'contact':'Contact Number ',
            'email':'Email-Id ',
            'requirement':'Specific Requirement ',
        }
        
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control mt-2'}),
            'lname':forms.TextInput(attrs={'class':'form-control mt-2'}),
            'contact':forms.NumberInput(attrs={'class':'form-control mt-2'}),
            'email':forms.EmailInput(attrs={'class':'form-control mt-2'}),
            'requirement':forms.Textarea(attrs={'class':'form-control mt-2'})
        }
        
        

class RegistrationForm(UserCreationForm):
    
    password1 = forms.CharField(label='Enter your password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm your password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        
        model = User
        
        fields = ["first_name","last_name","email"]
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            # 'contact_number': forms.NumberInput(attrs={'class':'form-control'}),
        }
        
        
        
class LoginForm(AuthenticationForm):
    
    email = forms.CharField(label='Enter your Email' , widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter your password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        
        model = User

        fields = ["email","password"]
        
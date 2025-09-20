from django import forms
from django.contrib.auth.models import User
from .models import userDetails
from django_recaptcha.fields import ReCaptchaField

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
        fields = ["username", "email", "password"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = ["Door_no", 'street', 'city', 'state', 'zipcode', 'profile_pic']
    captcha = ReCaptchaField()


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class UpdateDetailsForm(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = ["Door_no", 'street', 'city', 'state', 'zipcode', 'profile_pic']

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self):
        cleaned_date = super().clean()
        username = cleaned_date.get('username')
        # password = cleaned_date.get('password')
        password = cleaned_date['password']
        confirm_password = cleaned_date.get('confirm_password')
        
        if username:
            try:
                User.objects.get(username=username)
            except:
                raise forms.ValidationError("user does not exits")

        '''if password and confirm_password:
            try:
                if password != confirm_password:
                    raise forms.ValidationError("password and confirm password must be same")
                    # User.objects.get(password=password)
            except:
                pass'''

        if password != confirm_password:
            raise forms.ValidationError("password and confirm password must be same")
    
                

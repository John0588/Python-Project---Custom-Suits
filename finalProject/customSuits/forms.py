from django import forms

class contactUsForm(forms.Form):
 fName = forms.CharField(max_length=100, label='First Name:')
 lName = forms.CharField(max_length=100, label='Last Name:')
 email = forms.CharField(max_length=100, label='Email:', widget=forms.EmailInput)
 message = forms.CharField(max_length=100, label='Your Message:', widget=forms.PasswordInput)

class signUpForm(forms.Form):
 fName = forms.CharField(max_length=100, label='First Name:')
 lName = forms.CharField(max_length=100, label='Last Name:')
 email = forms.CharField(max_length=100, label='Email:', widget=forms.EmailInput)
 password = forms.CharField(max_length=100, label='Password:', widget=forms.PasswordInput)

class signInForm(forms.Form):
 email = forms.CharField(max_length=100, label='Email:', widget=forms.EmailInput)
 password = forms.CharField(max_length=100, label='Password:', widget=forms.PasswordInput) 
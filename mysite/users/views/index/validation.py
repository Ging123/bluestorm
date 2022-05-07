from django import forms

class CreateUserForm(forms.Form):
  
  email = forms.EmailField(
    max_length=100,
    required=True
  )
  
  password = forms.CharField(
    max_length=80,
    min_length=7,
    required=True
  )
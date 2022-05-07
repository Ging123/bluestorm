from django import forms

class LoginUserForm(forms.Form):

  email = forms.EmailField(
    max_length=100,
    required=True,
    error_messages={
      'max_length':"email doesn't exists"
    }
  )

  password = forms.CharField(
    max_length=80,
    min_length=7,
    required=True,
    error_messages={
      'max_length':'password is wrong',
      'min_length':'password is wrong'
    }
  )
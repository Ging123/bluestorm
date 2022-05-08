from django import forms

class GetTransactionValidation(forms.Form):

  page = forms.IntegerField(
    min_value=1,
    required=False,
    error_messages={ 'min_value':'invalid page' }
  )
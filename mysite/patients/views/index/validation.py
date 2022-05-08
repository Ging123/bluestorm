from django import forms

class GetPatientsValidation(forms.Form):

  page = forms.IntegerField(
    min_value=1,
    required=False,
    error_messages={ 'min_value':'invalid page' }
  )

  name = forms.CharField(
    required=False
  )

  birthday = forms.DateField(
    required=False
  )

  sort_by = forms.CharField(
    required=False
  )
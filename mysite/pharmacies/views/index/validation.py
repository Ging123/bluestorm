from django import forms

class GetPharmacyValidation(forms.Form):

  page = forms.IntegerField(
    min_value=1,
    required=False,
    error_messages={ 'min_value':'invalid page' }
  )

  name = forms.CharField(
    required=False
  )

  city = forms.CharField(
    required=False
  )

  sort_by = forms.CharField(
    required=False
  )
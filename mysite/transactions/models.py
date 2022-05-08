from pharmacies.models import Pharmacy
from patients.models import Patient
from django.db import models

class Transaction(models.Model):

  patient_id = models.ForeignKey(
    Patient, 
    on_delete=models.CASCADE
  )

  pharmacy_id = models.ForeignKey(
    Pharmacy,
    on_delete=models.CASCADE
  )

  quantity = models.FloatField(
    max_length=100000, 
    null=False
  )

  date = models.DateField( null=False )
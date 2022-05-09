from django.db import models

class Patient(models.Model):

  name = models.CharField(
    max_length=50,
    null=False
  )

  last_name = models.CharField(
    max_length=50,
    null=False
  )

  birthday = models.DateField(
    null=False
  )
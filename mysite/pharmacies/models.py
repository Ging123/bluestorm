from django.db import models

class Pharmacy(models.Model):

  name = models.CharField(
    max_length=100,
    null=False
  )

  city = models.CharField(
    max_length=100,
    null=False
  )
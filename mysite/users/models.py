from django.db import models

class User(models.Model):

  email = models.EmailField(
    max_length=100,
    unique=True
  )
  
  password = models.CharField(
    max_length=80
  )

  token = models.CharField(
    max_length=100
  )
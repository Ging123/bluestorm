from django.db import models

class User(models.Model):

  email = models.EmailField(
    db_index=True,
    max_length=100,
    null=False,
    unique=True
  )
  
  password = models.CharField(
    max_length=80,
    null=False
  )

  token = models.CharField(
    max_length=100
  )
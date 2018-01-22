from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(User):
  GENDER = (
    ('M', 'Male'),
    ('F', "Female")
  )
  birth_date = models.DateField(blank=True)
  gender = models.CharField(max_length=1, choices=GENDER)
  description = models.CharField("user's description", max_length=140)



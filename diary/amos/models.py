from django.db import models

# Create your models here.

class Person(models.Model):
  GENDER = (
    ('M', 'Male'),
    ('F', "Female")
  )
  SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
  )
  name = models.CharField("person's full name", max_length=30, unique=True)
  gender = models.CharField(max_length=1, choices=GENDER)
  shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)



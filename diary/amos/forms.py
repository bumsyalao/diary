from django.forms import ModelForm
from amos.models import Person

class PersonForm(ModelForm):
  class Meta:
    model = Person
    fields = ['name', 'gender', 'shirt_size']
from django.forms import ModelForm
from authorization.models import User

class RegisterForm(ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'password', 'birth_date', 'gender',  'description']
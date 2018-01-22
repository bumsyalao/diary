from django.shortcuts import render
from django.views.generic import TemplateView, View

from authorization.models import User
from authorization.forms import RegisterForm

# Create your views here.

def register(request):
  
  if request.method == "GET":
    context = {
      "form": RegisterForm()
    }
    return render(request, "authorization/register.html", context)
  elif request.method == "POST":
    form = RegisterForm(request.POST)

    if form.is_valid():
      user = form.save(commit=False)
      User.objects.create_user(user)
    return redirect('people')

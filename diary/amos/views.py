from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View

from amos.models import Person
from amos.forms import PersonForm
# Create your views here.

def index(request):
  # return HttpResponse("Hi Amos, welcome to my Diary App")
  context = {
    "books": [
      {"title": "Book 1"},
      {"title": "Book 2"},   
    ]
  }
  return render(request, "amos/index.html", context)



class PersonView(TemplateView):
  template_name = "amos/people.html"


  def get_context_data(self, *args, **kwargs):
    context = super(PersonView, self).get_context_data(**kwargs)

    context['people'] = Person.objects.all()

    form = PersonForm()

    context['form'] = form
    return context



# class  AddPerson(TemplateView):
def add_person(request):
  if request.method == "POST":
    form = PersonForm(request.POST)

    if form.is_valid():
      person = form.save(commit=False)
      person.save()

    # person = Person(name=name, gender=gender, shirt_size=shirt_size)
    # person.save()

    return redirect('people')
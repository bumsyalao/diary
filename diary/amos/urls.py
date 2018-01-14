from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name= 'index'),
  path('people', views.PersonView.as_view(), name='people'),
  path('addperson', views.add_person, name='addperson')
]
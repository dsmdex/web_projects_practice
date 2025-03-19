from django.shortcuts import render, get_object_or_404
from .models import State, Attraction
from .forms import CreateAttractionForm, CreateStateForm
from django.views.generic.edit import CreateView

def home(request):
  all_attractions = Attraction.objects.all()
  context = {"attractions" : all_attractions}
  return render(request, 'attractions/home.html', context)

def details(request, statename):
  attractions = Attraction.objects.all()
  context = {"attractions" : attractions, "statename" : statename.replace("-", " ")}
  return render(request, 'attractions/details.html', context)

class CreateStateView(CreateView):
  model = State
  template_name = 'attractions/state_create_form.html'
  form_class = CreateStateForm

class CreateAttractionView(CreateView):
  model = Attraction
  template_name = 'attractions/attraction_create_form.html'
  form_class =  CreateAttractionForm


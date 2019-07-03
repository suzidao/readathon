from django.shortcuts import render, redirect

from .models import Reader
from .forms import RegistrationForm

def index(request):
  participants = Reader.objects.order_by('name')
  context = {'participants': participants}
  return render(request, 'readers/index.html', context)

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      reader = form.save(commit=False)
      reader.save()
      return redirect('/readers')
  else:
    form = RegistrationForm()

  context = {'form': form}
  return render(request, 'readers/registration.html', context)
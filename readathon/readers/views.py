from django.shortcuts import render

from .models import Reader

def index(request):
  participants = Reader.objects.order_by('name')
  context = {'participants': participants}
  return render(request, 'readers/index.html', context)

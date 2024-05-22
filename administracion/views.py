from django.shortcuts import render
from django.http import HttpResponse
from .models import Horse

# Create your views here.
def index(request):
    horses= Horse.objects.all()
    return render(request, 'horses/index.html', {'horses': horses})

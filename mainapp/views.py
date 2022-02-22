from django.shortcuts import render
import random

# Create your views here.

def index(request):
    rnumber = random.randrange(0,6)
    return render(request,'mainapp/base.html', {'rnumber': rnumber})

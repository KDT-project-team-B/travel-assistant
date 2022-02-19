from django.shortcuts import render

# Create your views here.
def travelmain(request):
	    return render(request, 'travelapp/sample.html')
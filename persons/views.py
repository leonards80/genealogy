from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def persons_list(request):
    return render(request, "index.html", {})

def persons_details(request):
    return HttpResponse("<h1>Details</h1>")

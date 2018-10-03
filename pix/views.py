from django.shortcuts import render
from django.http  import HttpResponse

def index(request):
    """
    Function that renders the landing page
    """
    return render(request, 'index.html')
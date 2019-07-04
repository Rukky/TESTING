from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    return render(request, 'testsite/index.html')
def about(request):

    return render(request, 'testsite/index.html')
def opinions(request):

    return render(request, 'testsite/index.html')
def projects(request):

    return render(request, 'testsite/index.html')
def hadejia(request):

    return render(request, 'testsite/index.html')
def contact(request , FormData):
    try:
        Name = string(request.POST["Name"])

    return render()

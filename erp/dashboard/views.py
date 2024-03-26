from django.http import HttpResponse
from django.shortcuts import render

# include template loader
from django.template import loader


def index(request):
    # Load the template from the templates folder
    return render(request, "dashboard/index.html")


def test(request):
    # Load the template from the templates folder
    return render(request, "dashboard/test.html")

def test2(request):
    return HttpResponse("Hello, world. You're at the dashboard test2 page.")

from django.shortcuts import render


def index(request):
    # Load the template from the templates folder
    return render(request, "dashboard/index.html")

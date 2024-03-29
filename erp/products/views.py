from django.shortcuts import render

# Create your views here.
def index(request):
    # Load the template from the templates folder
    return render(request, "products/index.html")
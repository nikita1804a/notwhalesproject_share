from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def catalog(request):
    # context = {
    #     'products': Products().objects.all
    # }
    return render(request, 'catalog.html')
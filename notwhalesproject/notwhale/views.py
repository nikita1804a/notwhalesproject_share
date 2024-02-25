from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return render(request, 'helloworld.html')

def func_1(request):
    return render(request, 'one.html')

def func_2(request):
    return render(request, 'two.html')
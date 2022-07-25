from django.shortcuts import render


# Create your views here.
def resources(request):
    return render(request, 'resources/main.html')

def knowbank(request):
    return render(request, 'resources/bank.html')

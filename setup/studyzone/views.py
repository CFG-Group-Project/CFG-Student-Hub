from django.shortcuts import render
from .models import timeritem
# Create your views here.


def study(request):
    return render(request, 'studyzone/study.html')
    # return render(request, '/study.html')


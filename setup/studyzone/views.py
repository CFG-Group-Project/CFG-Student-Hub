from django.shortcuts import render

# Create your views here.


def study(request):
    return render(request, 'studyzone/study.html')
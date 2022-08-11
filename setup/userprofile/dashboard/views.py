from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from ..models import *


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    # if the user hasn't completed profile creation, they get redirected
    try:
        like_tally = Like.objects.filter(user=Profile.objects.get(user=request.user)).count
        comment_tally = Comment.objects.filter(user=Profile.objects.get(user=request.user)).count
        post_tally = Post.objects.filter(user=Profile.objects.get(user=request.user)).count
        context = {'posts': post_tally, 'comments': comment_tally, 'likes': like_tally}
        return render(request, 'dashboard/dashboard.html', context)
    # this exception clause is very broad, but it covers the possible exceptions that could be raised by the above
    # which would be solved by confirming profile info. when updating, remember to remove the exception handling to
    # be able to see the actual errors
    except Exception as e:
        return HttpResponseRedirect('profile')

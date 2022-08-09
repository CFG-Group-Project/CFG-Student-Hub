from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views import View
from django.core.paginator import Paginator

from .forms import ProfileForm, form_validation_error, PostForm, CommentForm
from .models import Profile, Post, Comment


# Create your views here.

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'userprofile/profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.username = form.cleaned_data.get('username')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.avatar = form.cleaned_data.get('avatar')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('/profile')


#  FORUM
@login_required(login_url='login')
def forum(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'post_list': post_list,
        'posts': posts,}
    return render(request, 'forum/forum.html', context)



class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {'post': post,
                   "form":form,
                   "comments":comments,
                   "title": "OZONE: " + post.title,
                   }

        return render(request, 'forum/discussion.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            author = Profile.objects.get(user=request.user)
            new_comment.post = post
            new_comment.user = author
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
        return render(request, 'forum/discussion.html', context)


def like_comment(request, slug):
    return redirect('/forum/')


@login_required(login_url='login')
def create_post(request):
    form = PostForm(request.POST or None)
    context = {'form': form}
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = Profile.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("/forum/my-posts")
        context.update({
            "form": form,
            "title": "OZONE: Create New Post"
        })
    return render(request, 'forum/create_post.html', context)


def my_posts(request):
    user = request.user.profile
    post_list = Post.objects.all().filter(user=user)
    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        "post_list": post_list,
        "title": "OZONE: My Posts",
        "posts": posts,
    }
    return render(request, "forum/my_posts.html", context)

def delete_post(request, id):
    context = {}
    obj = get_object_or_404(Post, id=id)
    Post.objects.get(id=id).delete()
    return HttpResponseRedirect('/forum/my-posts')

class AddCommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        liked = False

        for like in comment.likes.all():
            if like == request.user.profile:
                liked = True
                break

        if not liked:
            comment.likes.add(request.user.profile)

        if liked:
            comment.likes.remove(request.user.profile)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
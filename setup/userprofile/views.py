from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View


from .forms import ProfileForm, form_validation_error, PostForm
from .models import Profile, Category, Post, Comment, Reply


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
def forum(request):

    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'forum/forum.html', context)


def discussion(request, slug):
    post = Post.objects.get(slug=slug)


    if "comment-form" in request.POST:
        author = Profile.objects.get(user=request.user)
        comment = request.POST.get("content")
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

    context = {'post': post,
               "title": "OZONE: "+post.title,
               }

    return render(request, 'forum/discussion.html', context)


def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = Profile.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("home")
        context.update({
            "form": form,
            "title": "OZONE: Create New Post"
        })
    return render(request, 'forum/create_post.html', context)

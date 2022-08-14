from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('forum/', views.forum, name='forum'),
    path('forum/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('forum/<int:post_pk>/comment/<int:pk>/like', views.AddCommentLike.as_view(), name='comment-like'),
    path('forum/create-post', views.create_post),
    path('forum/my-posts', views.my_posts),
    path('forum/my-posts/delete/<int:id>',views.delete_post,name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
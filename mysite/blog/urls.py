from django.urls import path
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    path(r'', ListView.as_view(
                    queryset=Post.objects.all().order_by('-date'),
                    template_name='blog/blog.html')),
    path(r'<int:pk>/', DetailView.as_view(
                    model = Post,
                    template_name="blog/post.html")),
]

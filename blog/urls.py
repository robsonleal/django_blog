from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', BlogDetailView.as_view(), name='post_detail'),
]

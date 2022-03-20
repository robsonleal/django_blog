from django.urls import path
from blog.views import BlogListView, BlogDetailView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<slug:slug>', BlogDetailView.as_view(), name='post_detail'),
]

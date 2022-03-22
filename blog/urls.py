from django.urls import path
from blog.views import \
    BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView,\
    BlogDeleteView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/edit/<slug:slug>/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/del/<slug:slug>/', BlogDeleteView.as_view(), name='post_del'),
]

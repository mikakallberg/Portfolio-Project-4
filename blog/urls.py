from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

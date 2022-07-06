from . import views, forms
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', forms.CreatePostForm.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

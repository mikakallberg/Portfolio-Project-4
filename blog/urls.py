""" URL patterns connecting blog functionality"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path(
        'comment-update/<int:pk>',
        views.CommentUpdateView.as_view(),
        name='update_comment'
        ),
    path(
        'delete_comment/<slug:slug>/<int:pk>/',
        views.CommentDeleteView.as_view(),
        name='delete_comment'
        ),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path(
        '<slug:slug>/<int:pk>',
        views.CommentUpdateView.as_view(),
        name='update_comment'
        ),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

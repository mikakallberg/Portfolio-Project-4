from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import BlogPost


class PostList(generic.ListView):
    """ Settings for front view of blog """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'post_list'
    template_name = 'index.html'
    paginate_by = 6



class PostDetail(View):
    """ Settings for displaying individual BlogPosts and likes"""

    def get(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked,
            },
        )

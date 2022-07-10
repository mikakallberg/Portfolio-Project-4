from django.shortcuts import render, get_object_or_404, reverse
from django.utils.translation import gettext_lazy as _
from django.views import generic, View
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from .models import BlogPost, CommentSection
from .forms import CommentForm


class PostList(generic.ListView):
    """ Settings frontview of blog """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'post_list'
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """ Settings for displaying individual BlogPosts"""

    def get(self, request, slug, *args, **kwargs):
        """ Get information on Blogpost from backend """
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
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm(),
                'title': post.title,
            },
        )

    def post(self, request, slug, form, *args, **kwargs):
        """ Send information back to backend """
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        form.instance.created_by = self.request.user

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form,
                'liked': liked,
            },
        )


class CommentUpdateView(UpdateView):
    model = CommentSection
    form_class = CommentForm
    template_name_suffix = '_post_detail'
    template_name = 'post_detail.html'
    success_url = '/'


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(BlogPost, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

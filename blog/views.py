""" Rendering the functionality in user views """
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
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
                'form': CommentForm(),
                'title': post.title,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ Send information back to backend """
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = self.request.user
            form.email = request.user.email
            form.post = post
            form.save()
        else:
            form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'form': form,
                'liked': liked,
            },
        )

    def form_valid(self, form):
        """ validate form and connect to user """
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    """ Update comments via update_post.html """
    model = CommentSection
    form_class = CommentForm
    context_object_name = 'comment'
    template_name = 'update_post.html'

    def form_valid(self, form):
        """
        Success url return to blogpost in question
        with successfull commentform
        """
        self.success_url = f'/{self.get_object().post.slug}/'
        return super().form_valid(form)


class CommentDeleteView(DeleteView):
    """ Connects comment to DeleteView function """
    model = CommentSection
    template_name = 'delete_comment_post.html'
    context_object_name = 'comment'
    # success_url = reverse_lazy('post_detail')

    def get_success_url(self, *args):
        """ Success url return to blogpost in question """
        self.success_url = f'/{self.get_object().post.slug}'
        self.slug = self.get_object().post.slug
        return reverse_lazy('post_detail', args=[self.slug])


class PostLike(View):
    """ Remove or add like and redirect to post_detail.html """
    def post(self, request, slug, *args, **kwargs):
        """
        get object through slug,
        if user.id matches change status on like
        """
        post = get_object_or_404(BlogPost, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

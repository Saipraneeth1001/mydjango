
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth import get_user_model
from blog.forms import PostForm, CommentForm
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.contrib.auth import  get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
user = get_user_model()


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


# if he is not logged in then django will sent him to the login url
# if he is logged in then redirect him to post_detail page when this view is selected
# the form class statement allows user to edit the PostForm by adding data to it


class CreatePostView(LoginRequiredMixin, PermissionRequiredMixin, CreateView,):
    permission_required = 'user.is_staff'
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class UpdatePostView(LoginRequiredMixin, UpdateView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# query set returns the set completely , satisfying the given filter objects


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


# ---- functions with pk value -----
# the details from the model Post are stored in the variable post

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

# again in the below method we are adding the comment to our  post
# and for that we again stored the details of our model post into post variable
#  comment = form.save(commit=False) this method just stores the data in comment variable
# if the method is 'post' then after filling the comment form redirect to post_detail.html
# else form = CommentForm() i.e just show them a blank comment form ...
# which can be found in comment_form.html


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

# this method is defined to approve comments
# for now we stored all the comment form data in comment var
# this function calls the approve function again inside of it
# pk=comment.post.pk this means the pk is stored for a post not for a comment so ,
# we are accessing the pk from the post var we created above..


def index(request):
    return render(request, 'blog/index.html')

















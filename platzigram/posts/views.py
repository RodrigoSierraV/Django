from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from datetime import datetime
from posts.forms import PostForm
from posts.models import Post
import json
# Create your views here.


class PostFeedView(LoginRequiredMixin, ListView):

    template_name = 'posts/feed.html'
    model = Post
    ordering = '-created'
    paginate_by = 2
    context_object_name = 'posts'

#@login_required
#def list_posts(request):
#
#    posts = Post.objects.all().order_by('-created')
#
#    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(request,
                'posts/new.html',
                {'form': form, 'user': request.user, 'profile': request.user.profile})

#def list_posts(request):
#    content = []
#    for post in posts:
#        content.append("""
#        <p>{user}</p>
#        <img src={picture}>
#        <p>{name} {timestamp}</p>
#    """.format(**post))
#    return HttpResponse('<br>'.join(content))
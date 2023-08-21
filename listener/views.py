from django.shortcuts import render
from manager.models import Program,Post
import json

def home(request):
    if request.method == 'POST':
       print('mes')
    else:
      posts = Post.objects.all()[:20]
       
    context = {
        'posts' : posts,
        'program' : Program.objects.last()
    }
    return render(request, 'home.html', context)

def view_post(request, slug):
   context = {
      'post' : Post.objects.get(slug=slug)
   }
   return render(request, 'view_post.html', context)
from django.shortcuts import render
from django.http import JsonResponse
from manager.models import Program,Post
import json

def home(request):
   if request.method == 'POST':
      print('mes')
   else:
      posts = Post.objects.all()[:20]
   
   if Program.objects.count() > 1:
      next_program = Program.objects.order_by('start_date')[1]
   else:
      next_program = ''

   context = {
      'posts' : posts,
      'program' : Program.objects.order_by('start_date').first(),
      'next_program' : next_program,
   }
   return render(request, 'home.html', context)

def more_posts(request):
   return JsonResponse({'test':'good'})

def view_post(request, slug):
   context = {
      'post' : Post.objects.get(slug=slug)
   }
   return render(request, 'view_post.html', context)

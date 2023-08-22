from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from datetime import timedelta
from manager.models import Program,Post
import json

def home(request):
   if request.method == 'POST':
      print('mes')
   else:
      posts = Post.objects.all()[:20]
   
   if Program.objects.count() > 1:
      next_program = Program.objects.filter().order_by('start_date')[1]
   else:
      next_program = '' 

   context = {
      'token' : get_token(request),
      'posts' : posts,
      'posts_rev' : Post.objects.all().order_by('-id')[:9],
      'program' : Program.objects.order_by('start_date').first(),
      'next_program' : next_program,
   }
   return render(request, 'home.html', context)

def more_posts(request):
   return JsonResponse({'test':'good'})

def view_post(request, slug):
   if Program.objects.count() > 1:
      next_program = Program.objects.filter().order_by('start_date')[1]
   else:
      next_program = '' 
   context = {
      'post' : Post.objects.get(slug=slug),
      'program' : Program.objects.order_by('start_date').first(),
      'next_program' : next_program
   }
   return render(request, 'view_post.html', context)

def schedule_program(request):
   json_data = json.loads(request.body)['data']
   program = Program.objects.get(id=int(json_data))
   program.start_date = program.start_date + timedelta(days=7)
   program.end_date = program.end_date + timedelta(days=7)
   program.save()
   return JsonResponse({'test':'schedule'})
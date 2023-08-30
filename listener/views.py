from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from datetime import timedelta
from manager.models import Program,Post
from django.template.defaultfilters import timesince
import json

def home(request):
   if request.method == 'POST':
      posts = Post.objects.filter(category=request.POST.get('category'))[:20]
   else:
      posts = Post.objects.all().order_by('-date_added')[:20]
   
   if Program.objects.count() > 1:
      next_program = Program.objects.filter().order_by('start_date')[1]
   else:
      next_program = '' 

   context = {
      'token' : get_token(request),
      'posts' : posts,
      'posts_rev' : Post.objects.filter(type='image').order_by('-id')[:9],
      'popular_posts' : Post.objects.order_by('-impressions')[:5],
      'program' : Program.objects.order_by('start_date').first(),
      'next_program' : next_program,
      'post_count' : Post.objects.all().count()
   }
   return render(request, 'home.html', context)

def more_posts(request):
   json_data = json.loads(request.body)['data']
   x = int(json_data) 
   post_box = []
   posts = Post.objects.all().order_by('-date_added')[:x+20]

   for post in posts:
      post_el = {}
      post_el['slug'] = post.slug
      post_el['title'] = post.title
      post_el['time_since'] = timesince(post.date_added)
      post_el['tags'] = post.tags
      post_el['category'] = post.category
      post_el['type'] = post.type
      if post.type == 'image':
         post_el['media_url'] = post.image.url
      else:
         post_el['media_url'] = post.video.url
      post_el['source'] = post.source
      post_el['content'] = post.content
      post_box.append(post_el)
   
   return JsonResponse({'test':json.dumps(post_box)})

def view_post(request, slug):
   post = Post.objects.get(slug=slug)
   union_posts = Post.objects.filter(category=post.category).exclude(id=post.id)
   if union_posts.count() < 4:
      union_posts = Post.objects.exclude(category=post.category) | Post.objects.filter(category=post.category).exclude(id=post.id)

   if Program.objects.count() > 1:
      next_program = Program.objects.filter().order_by('start_date')[1]
   else:
      next_program = '' 
   context = {
      'post' : post,
      'program' : Program.objects.order_by('start_date').first(),
      'popular_posts' : Post.objects.order_by('-impressions')[:5],
      'relateds' : union_posts[:4],
      'next_program' : next_program
   }
   return render(request, 'view_post.html', context)

def add_post_impression(request):
   json_data = json.loads(request.body)['data']
   post = Post.objects.get(id=int(json_data))
   post.impressions += 1
   post.save()
   return JsonResponse({'test':'impressed'})


def view_program(request, id):
   program = Program.objects.get(id=id)
   if Program.objects.count() > 1:
      next_program = Program.objects.filter().order_by('start_date')[1]
   else:
      next_program = '' 
   context = {
      'program' : program,
      'relateds' : Program.objects.order_by('-start_date').exclude(name=program.name)[:4],
      'next_program' : next_program,
      'popular_posts' : Post.objects.order_by('-impressions')[:5],
   }
   return render(request, 'view_program.html', context)

def schedule_program(request):
   json_data = json.loads(request.body)['data']
   program = Program.objects.get(id=int(json_data))
   program.start_date = program.start_date + timedelta(days=7)
   program.end_date = program.end_date + timedelta(days=7)
   program.save()
   return JsonResponse({'test':'schedule'})

def contact(request):
   context = {
      'token' : get_token(request),
      'program' : Program.objects.order_by('start_date').first(),
   }
   return render(request, 'contact.html', context)

def about(request):
   context = {
      'token' : get_token(request),
      'program' : Program.objects.order_by('start_date').first(),
   }
   return render(request, 'about.html', context)

def terms(request):
   context = {
      'token' : get_token(request),
      'program' : Program.objects.order_by('start_date').first(),
   }
   return render(request, 'terms.html', context)
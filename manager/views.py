from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.middleware.csrf import get_token
from .models import Program,Post
from datetime import datetime,timedelta
import json

def manager(request):
    context = {
        'programs' : Program.objects.all()[:5],
        'posts' : Post.objects.all()[:5]
    }
    return render(request, 'manager.html', context)

def fix_prog_json(prog):
    prog_json = {}
    prog_json['id'] = prog.id
    prog_json['name'] = prog.name
    prog_json['description'] = prog.description
    prog_json['host'] = prog.host
    prog_json['start_date'] = prog.start_date.strftime('%Y-%m-%d %H:%M:%S')
    prog_json['end_date'] = prog.end_date.strftime('%Y-%m-%d %H:%M:%S')
    prog_json['image_url'] = prog.image.url
    return prog_json

def create_program(request, program):
    prog_day = int(request.POST.get('py_day'))
    current_date = datetime.today()
    days_to = (prog_day - current_date.weekday()) % 7
    prog_date = (current_date + timedelta(days=days_to)).strftime('%Y-%m-%d %H:%M:%S')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    program.name = request.POST.get('name').upper()
    program.description = request.POST.get('description')
    program.host = request.POST.get('host')
    program.start_date = datetime.strptime(prog_date.split(' ')[0] + f' {start_time}', "%Y-%m-%d %H:%M")
    program.end_date = datetime.strptime(prog_date.split(' ')[0] + f' {end_time}', "%Y-%m-%d %H:%M")
    return program

def programs(request):
    prog_box = []
    for prog in Program.objects.all().order_by('start_date'):
        prog_box.append(fix_prog_json(prog))
    
    if request.method == 'POST':
        if int(request.POST['id']) == 0:
            program = create_program(request, Program())
            program.image = request.FILES['image']
            program.save()
            return redirect('programs_page')
        else:
            program = create_program(request, Program.objects.get(id=int(request.POST.get('id'))))
            if 'image' in request.FILES:
                program.image = request.FILES['image']
            program.save()
            return redirect('programs_page')
    context = {
        'token' : get_token(request),
        'prog_box' : json.dumps(prog_box)
    }
    return render(request, 'programs.html', context)

def del_program(request):
    json_data = json.loads(request.body)['data']
    Program.objects.get(id=int(json_data)).delete()
    return JsonResponse({'test':'good'})

def create_post(request, post):
    post.title = request.POST.get('title')
    post.category = request.POST.get('category')
    post.content = request.POST.get('content')
    post.source = request.POST.get('source')
    post.tags = request.POST.get('tags')
    return post

def posts(request):
    if request.method == 'POST':
        if int(request.POST.get('id')) == 0:            
            post = create_post(request, Post())
            if 'image' in request.FILES:
                post.type = 'image'
                post.image = request.FILES['image']
            else:
                post.type = 'video'
                post.video = request.FILES['video']
            post.save()
            return redirect('posts_page')
        else:
            post = create_post(request, Post.objects.get(id=int(request.POST.get('id'))))
            if 'image' in request.FILES:
                post.type = 'image'
                post.image = request.FILES['image']
            elif 'video' in request.FILES:
                post.type = 'video'
                post.video = request.FILES['video']
            post.save()
            return redirect('posts_page')
    context = {
        'token' : get_token(request),
        'posts' : Post.objects.all()
    }
    return render(request, 'posts.html', context)

def del_post(request):
    json_data = json.loads(request.body)['data']
    Post.objects.get(id=int(json_data)).delete()
    return JsonResponse({'test':'good'})
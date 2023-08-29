from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),

    path('view_post/<slug>', views.view_post, name='view_post_page'),
    path('more_posts', views.more_posts),
    path('add_post_impression', views.add_post_impression),

    path('view_program/<id>', views.view_program, name='view_program_page'),
    path('schedule_program', views.schedule_program)
]

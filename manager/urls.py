from django.urls import path
from . import views

urlpatterns = [
    path('manager', views.manager, name='manager_page'),

    path('programs', views.programs, name='programs_page'),
    path('del_program', views.del_program),

    path('posts', views.posts, name='posts_page'),
    path('del_post', views.del_post),
]

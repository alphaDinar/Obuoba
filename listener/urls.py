from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('view_post/<slug>', views.view_post, name='view_post_page')
]

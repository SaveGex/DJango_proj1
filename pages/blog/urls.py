from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_index, name='index'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    path('create/', views.create_view, name= 'create')
]
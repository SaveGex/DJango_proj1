from django.shortcuts import render

from .models import Post 
# Create your views here.
def blog_index(request):

    all_posts = Post.objects.all()
    
    context = {
        "all_posts": all_posts
    }
    return render(request, "blog/index.html", context) # kpei4ny genius of this program 
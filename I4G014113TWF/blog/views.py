from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'home.html', {})

def post(request):
    bps = Post.objects.all().order_by('Created_date')
    return render(request, 'post.html', {'bp':bps})

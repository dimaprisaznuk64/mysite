from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("<h1>Це сторінка About</h1><p>Мій перший Git-проєкт!</p>")

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

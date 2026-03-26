from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.
from .models import Post

from . form import Postform



def post_list(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            form.save()  # Saves directly to SQLite3
            return redirect('post_list')  # Redirect after saving
    else:
        form = Postform()
    return render(request, 'post_list.html', {'posts': posts,'form':form})

def post_detail(request,pk):

    post =get_object_or_404(Post,pk=pk)
    

    return render(request, 'post_detail.html', {'post': post})



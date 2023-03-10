from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

from django.views.generic.edit import DeleteView

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/home.html', {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogapp/post_detail.html', {"post": post})


def post_create(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # post.publication_date= timezone.now()
            return redirect('post_detail', pk=post.pk)

    context = {"form": form}
    return render(request, 'blogapp/post_create.html', context)


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"post": post, "form": form}
    return render(request, 'blogapp/post_update.html', context)


# def post_delete(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     post.delete()
#     return redirect('home')
#
#     context = {"post": post}
#     return render(request, 'blogapp/post_delete.html', context)

class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = 'blogapp/post_delete.html'
# success_url = reverse_lazy('home')

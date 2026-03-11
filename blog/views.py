from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like , Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


from django.core.paginator import Paginator

def home(request):
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 4)  # posts per page
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category_id = request.POST.get("category")
        image = request.FILES.get("image")
        image_url = request.POST.get("image_url")

        Post.objects.create(
            title=title,
            content=content,
            category_id=category_id,
            author=request.user,
            image=image,
            image_url=image_url
        )
        return redirect("home")

    return render(request, "blog/create_post.html", {
        "categories": Category.objects.all()
    })



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')
    liked = False

    if request.user.is_authenticated:
        liked = Like.objects.filter(post=post, user=request.user).exists()

    if request.method == "POST":
        name = request.POST.get("name")
        body = request.POST.get("body")
        Comment.objects.create(post=post, name=name, body=body)
        return redirect('post_detail', post_id=post.id)

    context = {
        "post": post,
        "comments": comments,
        "liked": liked,
        "total_likes": post.likes.count(),
    }

    return render(request, "blog/post_detail.html", context)


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(post=post, user=request.user)

    if like.exists():
        like.delete()
    else:
        Like.objects.create(post=post, user=request.user)

    return redirect('post_detail', post_id=post.id)


def search(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

    return render(request, "blog/search.html", {
        "query": query,
        "results": results
    })
def category_posts(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    category = Category.objects.get(id=category_id)
    return render(request, "blog/category.html", {
        "category": category,
        "posts": posts,
    })
class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'category']
    template_name = "blog/post_edit.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user.is_superuser or self.request.user.is_staff



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("home")
    template_name = "blog/post_delete.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user.is_superuser or self.request.user.is_staff

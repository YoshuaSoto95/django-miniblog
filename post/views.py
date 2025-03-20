from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment, Category, Tag
from django.contrib import messages

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render(request, 'post_list.html', context)

def admin_post(request):
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render(request, 'admin_post.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = { 'post': post }
    return render(request, 'post_detail.html', context)

def add_post(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        imagen = request.FILES.get('imagen')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        tags_id = request.POST.getlist('tags')

        if title and subtitle and description and imagen and content and category_id and tags_id:
            category = Category.objects.get(id=category_id)
            post = Post.objects.create(
                title=title,
                subtitle=subtitle,
                description=description,
                imagen=imagen,
                content=content,
                category=category
            )
            post.tags.add(*tags_id)
            post.save()
            messages.success(request, 'Post created successfully')
            return redirect('post:post_list')
        else:
            messages.error(request, "All fields are required")
            return redirect('post:add_post')

    context = { 'categories': categories, 'tags': tags }
    return render(request, 'add_post.html', context)

def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = { 'categories': categories, 'tags': tags , 'post': post }

    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        imagen = request.FILES.get('imagen', '')
        content = request.POST.get('content')
        category_id = request.POST.get('category', '',)
        tags_id = request.POST.getlist('tags', '',)

        if title and subtitle and description and content:
            post.title = title
            post.subtitle = subtitle
            post.description = description
            post.content = content

            if imagen:
                post.imagen = imagen

            if category_id:
                category = Category.objects.get(id=category_id)
                post.category = category
            
            if tags_id:
                post.tags.clear()
                post.tags.add(*tags_id)

            post.save()
            messages.success(request, 'Post updated successfully')
            return redirect('post:post_list')
        else:
            messages.error(request, "All fields are required")
            return redirect('post:edit_post', slug=slug)

    return render(request, 'edit_post.html', context)

def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('post:admin_post')

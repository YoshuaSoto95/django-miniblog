from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment, Category, Tag
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# ====================================================================================== # POST
def post_list(request):
    posts = Post.objects.all().order_by('-create_at')
    context = { 'posts': posts }
    return render(request, 'post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = { 'post': post }
    return render(request, 'post_detail.html', context)

@login_required
def admin_post(request):
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render(request, 'admin_post.html', context)

@login_required
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

@login_required
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

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('post:admin_post')

# ====================================================================================== # END POST

# ====================================================================================== # CATEGORY

@login_required
def admin_categories(request):
    categories = Category.objects.all()
    context = { 'categories': categories }
    return render(request, 'admin_categories.html', context)

@login_required
def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            messages.success(request, 'Category created successfully')
            return redirect('post:admin_categories')
        else:
            messages.error(request, "All fields are required")
            return redirect('post:admin_categories')
    return render(request, 'admin_categories.html')

@login_required
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        name = request.POST.get('name')

        if name:
            category.name = name
            category.save()
            messages.success(request, 'Category updated successfully')
            return redirect('post:admin_categories')
        else:
            messages.error(request, "All fields are required")
            return redirect('post:admin_categories')
    return render(request, 'admin_categories.html')

@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, 'Category deleted successfully')
    return redirect('post:admin_categories')

# ====================================================================================== # END CATEGORY

# ====================================================================================== # TAGS

@login_required
def admin_tags(request):
    tags = Tag.objects.all()
    context = { 'tags': tags }
    return render(request, 'admin_tags.html', context)

@login_required
def add_tag(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Tag.objects.create(name=name)
            messages.success(request, 'Tag created successfully')
            return redirect('post:admin_tags')
        else:
            messages.error(request, "All fields are required")
            return redirect('post:admin_tags')
    return render(request, 'admin_tags.html')

@login_required
def edit_tag(request, id):
    tag = get_object_or_404(Tag, id=id)

    if request.method == "POST":
        name = request.POST.get('name')

        if name:
            tag.name = name
            tag.save()
            messages.success(request, 'Tag updated successfully')
            return redirect('post:admin_tags')
        else:
            messages.error(request, "All fields are required")
            return redirect('post:admin_tags')
    return render(request, 'admin_tags.html')

@login_required
def delete_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    tag.delete()
    messages.success(request, 'Tag deleted successfully')
    return redirect('post:admin_tags')

# ====================================================================================== # END TAGS

# ====================================================================================== # USERS

def admin_users(request):
    users = User.objects.all()
    context = { 'users': users }
    return render(request, 'admin_users.html', context)

def add_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('post:admin_users')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('post:admin_users')
                else:
                    User.objects.create_user(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password1
                    )
                    messages.success(request, 'User created successfully')
                    return redirect('post:admin_users')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('post:admin_users')
    return render(request, 'admin_users.html')

def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        if username and first_name and last_name and email:
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            messages.success(request, 'User updated successfully')
            return redirect('post:admin_users')
        else:
            messages.error(request, "All fields are required")
            return redirect('post:admin_users')
    return render(request, 'admin_users.html')


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, 'User deleted successfully')
    return redirect('post:admin_users')

# ====================================================================================== # END USERS


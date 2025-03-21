from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'), # list post in blog main
    path('<slug:slug>', views.post_detail, name='post_detail'), # view post detail in blog 

    # login_required
    # Posts
    path('add_post/', views.add_post, name='add_post'), # add_post 
    path('admin_post/', views.admin_post, name='admin_post'), # table with all post
    path('edit_post/<slug:slug>', views.edit_post, name='edit_post'), # edit post
    path('delete_post/<slug:slug>', views.delete_post, name='delete_post'), # delete post

    # Category
    path('admin_categories/', views.admin_categories, name='admin_categories'), # table with all category
    path('add_category/', views.add_category, name='add_category'), # add category
    path('edit_category/<int:id>', views.edit_category, name='edit_category'), # edit category
    path('delete_category/<int:id>', views.delete_category, name='delete_category'), # delete category

    # Tags
    path('admin_tags/', views.admin_tags, name='admin_tags'), # table with all tags
    path('add_tag/', views.add_tag, name='add_tag'), # add tag
    path('edit_tag/<int:id>', views.edit_tag, name='edit_tag'), # edit tag
    path('delete_tag/<int:id>', views.delete_tag, name='delete_tag'), # delete tag

    # Users
    path('admin_users/', views.admin_users, name="admin_users"), # table with all users
    path('add_user/', views.add_user, name="add_user"), # add user
    path('edit_user/<int:id>', views.edit_user, name="edit_user"), # edit user
    path('delete_user/<int:id>', views.delete_user, name="delete_user"), # delete user
]

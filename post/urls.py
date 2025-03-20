from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'), # list post in blog main
    path('add_post/', views.add_post, name='add_post'), # add_post 
    path('admin_post/', views.admin_post, name='admin_post'), # table with all post
    path('<slug:slug>', views.post_detail, name='post_detail'), # view post detail
    path('edit_post/<slug:slug>', views.edit_post, name='edit_post'), # edit post
    path('delete_post/<slug:slug>', views.delete_post, name='delete_post'), # delete post
]

from django.contrib import admin
from .models import Category, Tag, Post, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('create_at',)
    list_display = ('name', 'create_at',)

class TagAdmin(admin.ModelAdmin):
    exclude = ('create_at',)
    list_display = ('name', 'create_at',)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    exclude = ('create_at',)
    list_display = ('title', 'subtitle', 'description', 'imagen', 'category', 'slug', 'create_at',)

class CommentAdmin(admin.ModelAdmin):
    exclude = ('create_at',)
    list_display = ('post', 'name', 'text', 'create_at',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
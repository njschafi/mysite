from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    #model = Post.categories.through

class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-Empty Field-'
    inlines = [CategoryInline,]

class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-Empty Field-'
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

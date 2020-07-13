from django.contrib import admin
from .models import Blogs ,PostImage
# Register your models here.


class PostImageAdmin(admin.StackedInline):
    model=PostImage

@admin.register(Blogs)
class PostAdmin(admin.ModelAdmin):
    inlines =[PostImageAdmin]

    class Meta:
        model=Blogs

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
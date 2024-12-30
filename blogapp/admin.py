from django.contrib import admin

from blogapp.models import Utilisateur, PostCategory, Post, Comment


# Register your models here.
@admin.register(Utilisateur)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'image', 'password')


@admin.register(PostCategory)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display = ('titre',)

@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','commentaire')
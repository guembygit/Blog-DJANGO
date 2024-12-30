from django import forms
from django.http import request

from blogapp.models import Utilisateur, PostCategory, Post, Comment


class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Utilisateur
        fields = ("username", "email", "password", "image")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "name": "username",
            }), )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "name": "email",
            }), )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "name": "password",
            }), )
    image = forms.CharField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control form-control-sm",
                "name": "image",
            }), )


class AuthForm(forms.ModelForm):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40)

    class Meta:
        model = Utilisateur
        fields = ("username", "password")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "name": "username",
            }), )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "name": "password",
            }), )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titre", "slug", "category_id", "description", "image_post")

    titre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "name": "titre",
            }), )
    slug = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "name": "slug",
            }), )
    category_id = forms.ModelChoiceField(widget=forms.Select(
            attrs={
                "class": "form-control form-control-sm",
                "name": "category_id",
            }),queryset=PostCategory.objects.all())
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control form-control-sm",
                "name": "description",
            }), )
    image_post = forms.CharField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control form-control-sm",
                "name": "image_post",
            }), )


class UpCatForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
    commentaire = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "name": "commentaire",
                    "placeholder":"Commentaire"

                }), )


class UpUserForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = "__all__"

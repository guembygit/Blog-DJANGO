from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from pyexpat.errors import messages

from blogapp.forms import UserForm, AuthForm, PostForm, CommentForm, UpCatForm
from blogapp.models import Utilisateur, Post, PostCategory, Comment


# Create your views here.
def index(request):
    blog = Post.objects.all()
    context = PostCategory.objects.all()
    get_session = request.session['user_id']
    user = Utilisateur.objects.get(id=get_session)
    return render(request, 'blogapp/index.html',
                  {'blog': blog, 'context': context, 'get_session': get_session, 'user': user})


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        image = request.FILES['image']
        password = request.POST['password']
        user = Utilisateur.objects.create(username=username, email=email, image=image, password=password)
        if user:
            user.save()
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('index'))

    else:
        form = UserForm()
    return render(request, 'blogapp/register.html', {'form': form})


@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Utilisateur.objects.filter(username=username, password=password).values()
        if user:
            blogeur = Utilisateur.objects.get(username=username)
            blogeur_id = blogeur.id
            request.session['user_id'] = blogeur_id
            return HttpResponseRedirect(reverse('index'))
        else:
            print('le traitement à échouer ')
    form = AuthForm(request.POST)
    return render(request, 'blogapp/login.html', {'form': form})


@csrf_protect
def createpost(request):
    if request.method == "POST":
        titre = request.POST['titre']
        slug = request.POST['slug']
        category_ids = request.POST['category_id']
        description = request.POST['description']
        image_post = request.FILES['image_post']
        id_user = request.POST['user_id']
        id_user = Utilisateur.objects.get(id=id_user)
        category_ids = PostCategory.objects.get(id=category_ids)
        post = Post.objects.create(titre=titre, slug=slug, category_id=category_ids, description=description,
                                   image_post=image_post, user_id=id_user)
        if post:
            post.save()
            return HttpResponseRedirect(reverse('index'))

    get_session = request.session['user_id']
    form = PostForm()
    return render(request, 'blogapp/createpost.html', {'form': form, 'get_session': get_session})


def edit(request, id):
    one_post = Post.objects.get(id=id)
    categories = PostCategory.objects.all()
    return render(request, 'blogapp/update.html', {'one_post': one_post, 'categories': categories})


def update(request, id):
    one_post = Post.objects.get(id=id)
    post = UpCatForm(request.POST, instance=one_post)
    one_post.titre = request.POST['titre']
    one_post.slug = request.POST['slug']
    one_post.category_ids = request.POST['category_id']
    one_post.description = request.POST['description']
    one_post.image_post = request.FILES['image_post']
    one_post.id_user = request.POST['user_id']
    if post:
        one_post.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'blogapp/update.html', {'one_post': one_post, })


def destroy(request, id):
    employee = Post.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect(reverse('index'))


def post_id(request, pk):
    if request.method == "POST":
        id_user = request.POST['user_id']
        id_post = request.POST['post_id']
        commentaire = request.POST['commentaire']
        user_id = Utilisateur.objects.get(id=id_user)
        post_id = Post.objects.get(id=id_post)
        comment = Comment.objects.create(user_id=user_id, post_id=post_id, commentaire=commentaire)
        if comment:
            comment.save()
        else:
            print('erreur')
    post = Post.objects.get(id=pk)
    com = Comment.objects.filter(post_id=pk)
    form = CommentForm()
    get_session = request.session['user_id']
    return render(request, 'blogapp/post.html',
                  {'post': post, 'com': com, 'form': form, 'get_session': get_session, 'messages': messages})


def editcomment(request, id):
    one_com = Comment.objects.get(id=id)
    categories = Post.objects.get(id=id)
    get_session = request.session['user_id']
    return render(request, 'blogapp/updatecom.html',
                  {'one_com': one_com, 'categories': categories, 'get_session': get_session})


def updatecomment(request, id):
    one_post = Comment.objects.get(id=id)
    post = CommentForm(request.POST, instance=one_post)
    id_user = request.POST['user_id']
    id_post = request.POST['post_id']
    one_post.user_id = Utilisateur.objects.get(id=id_user)
    one_post.post_id = Post.objects.get(id=id_post)
    one_post.commentaire = request.POST['commentaire']
    if post:
        one_post.save()
        return HttpResponseRedirect(reverse('index'))


def destroycomment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(reverse('index'))


def propos(request):
    return render(request, 'blogapp/propos.html')


def category(request, id):
    com = Post.objects.filter(category_id=id)
    context = PostCategory.objects.all()
    return render(request, 'blogapp/category.html',
                  {'com': com, 'context': context})


def search_results(request):
    query = request.GET.get('query')
    results = Post.objects.filter(titre__icontains=query)
    return render(request, 'blogapp/search.html', {'results': results})


def deconnect(request):
    del request.session['user_id']
    return HttpResponseRedirect(reverse('login'))


def updateuser(request, id):
    one_user = Utilisateur.objects.get(id=id)
    users = UserForm(request.POST, instance=one_user)
    one_user.username = request.POST['username']
    one_user.email = request.POST['email']
    one_user.image = request.FILES['image']
    one_user.password = request.POST['password']
    if users :
        one_user.save()
        return HttpResponseRedirect(reverse('index'))

    form = UserForm()
    return render(request, 'blogapp/userupdate.html', {'form': form})

def edituser(request, id):
    one_user = Utilisateur.objects.get(id=id)
    return render(request, 'blogapp/userupdate.html', {'one_user': one_user})

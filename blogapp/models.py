from django.db import models


# Create your models here.
class Utilisateur(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to='Images')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{id} {username}, email={email}, password={password},image={image}, created={created}'.format(
            id=self.pk,
            username=self.username,
            email=self.email,
            password=self.password,
            image=self.image,
            created=self.created)


class PostCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)


class Post(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    user_id = models.ForeignKey('Utilisateur'
                                , on_delete=models.CASCADE)
    category_id = models.ForeignKey('PostCategory'
                                    , on_delete=models.CASCADE)
    description = models.TextField()
    image_post = models.ImageField(null=True, blank=True, upload_to='Images')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{id} {titre}, slug={slug}, user_id={user_id},description={description}, created={created}'.format(
            id=self.pk,
            titre=self.titre,
            slug=self.slug,
            user_id=self.user_id,
            description=self.description,
            created=self.created)


class Comment(models.Model):
    user_id = models.ForeignKey('Utilisateur'
                                , on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post',
                                on_delete=models.CASCADE)
    commentaire = models.TextField()
    created = models.DateTimeField(auto_now_add=True)



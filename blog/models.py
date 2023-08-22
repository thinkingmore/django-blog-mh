from django.db import models
from django.utils.text import slugify

from accounts.models import User

class Category(models.Model):
    title = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tags(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Tags'  

class Blog(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_blogs',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        related_name='category_blogs',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        Tags,
        related_name='tag_blogs',
        blank=True
    )
    likes = models.ManyToManyField(
        User,
        related_name='user_likes',
        blank=True
    )
    title = models.CharField(
        max_length=250,
    )
    slug = models.SlugField(
        null=True,
        blank=True,
    )
    banner  = models.ImageField(upload_to="blog-baanners")
    description = models.TextField()       
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_comments',
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name='blog_comments',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

class Replies(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_replies',
        on_delete=models.CASCADE
    )
    comment= models.ForeignKey(
        Comment,
        related_name='comment_replies',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Replies'
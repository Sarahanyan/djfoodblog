from django.db.models.base import Model
from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    servings = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(
        'Category', blank=True, related_name="recipeslist")
    blogpost = models.OneToOneField(
        'BlogPost', on_delete=models.SET_NULL, null=True, blank=True, related_name="recipe")
    ingredients = models.TextField()
    steps = models.TextField()
    calories = models.CharField(max_length=20)
    carbs = models.CharField(max_length=10)
    protein = models.CharField(max_length=10)
    fibre = models.CharField(max_length=10)
    fat = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]


class Review(models.Model):
    name = models.CharField(max_length=20)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    email = models.EmailField()
    comment = models.TextField()
    votes = models.IntegerField()

    def __str__(self):
        return self.name

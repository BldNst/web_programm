from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} - {self.title}'


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.article}'


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.pk} - {self.name}'

    @property
    def count(self):
        return self.article_set.count()
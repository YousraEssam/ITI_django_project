from django.db import models
from django.contrib.auth.models import User
from website.models import City

# Create your models here.

class Article(models.Model):
    article_id = models.PositiveIntegerField(primary_key=True)
    article_content = models.CharField(max_length=250,null=False)
    article_rank = models.IntegerField()
    city = models.ForeignKey(City)
    user = models.ForeignKey(User)


class Comment(models.Model):
    comment_id = models.PositiveIntegerField(primary_key=True)
    comment_content = models.CharField(max_length=250, null=False)
    comment_rank = models.IntegerField()
    article_id = models.ForeignKey(Article)
    user = models.ForeignKey(User)

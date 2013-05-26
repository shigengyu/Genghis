from django.db import models
from django.db.models.base import Model

# Create your models here.

class ArticleTag(Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length = 20),
    display_name = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.name


class Article(Model):
    id = models.AutoField(primary_key=True),
    subject = models.CharField(max_length = 256),
    content = models.TextField(),
    author = models.CharField(max_length = 50),
    create_date_time = models.DateTimeField(),
    update_date_time = models.DateTimeField(),
    tags = models.ManyToManyField(ArticleTag)
    
    def __unicode__(self):
        return self.subject


class ArticleComment(Model):
    id = models.AutoField(primary_key=True),
    article = models.ForeignKey(Article),
    subject = models.CharField(max_length = 256),
    content = models.TextField(),
    create_date_time = models.DateTimeField(),
    update_date_time = models.DateTimeField(),
    
    def __unicode__(self):
        return self.subject

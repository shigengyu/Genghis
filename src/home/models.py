from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class HomeModel(Model):
    title = "Univer's Blog"

class PathItem:
    
    def __init__(self, name):
        self.name = name
    
    def __init__(self, url, name):
        self.url = url
        self.name = name

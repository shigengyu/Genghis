from time import time
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

def get_file_upload_name(instance, filename):
    filename = "%s_%s" % (str(time()).replace('.', '_'), filename)
    return filename

class FileTag(Model):
    name = models.CharField(max_length=20)
    display_name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name

class File(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to=get_file_upload_name)
    uploaded_by = models.ForeignKey(User)
    upload_date_time = models.DateTimeField()
    tags = models.ManyToManyField(FileTag)
    
    def __unicode__(self):
        return self.name
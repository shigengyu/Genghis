from datetime import datetime
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

def get_file_upload_name(instance, filename):
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    filename = filename.replace(' ', '_')
    filename = "files/%s_%s" % (timestamp, filename)
    return filename

class File(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to=get_file_upload_name)
    uploaded_by = models.ForeignKey(User)
    upload_date_time = models.DateTimeField()
    
    def __unicode__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        storage, path = self.attachment.storage, self.attachment.path
        super(File, self).delete(*args, **kwargs)
        storage.delete(path)

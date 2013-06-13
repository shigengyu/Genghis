from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from genghis.settings import ADMINS
from django.contrib.auth.models import User

class RequireLogin(object):
    
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        if (not self.instance.request.user.is_authenticated()):
            return_url = self.instance.request.get_full_path()
            return HttpResponseRedirect('/home/login?next=' + return_url)
        
        result = self.func.__call__(self.instance, *args, **kwargs)
        return result
    
    def __get__(self, instance, owner):
        self.owner = owner
        self.instance = instance
        return self.__call__

class RequireAdmin(RequireLogin):
    
    def __call__(self, *args, **kwargs):
        if (not is_admin(self.instance.request.user)):
            return HttpResponseForbidden()
        
        result = self.func.__call__(self.instance, *args, **kwargs)
        return result

def is_admin(user):
    return user.is_authenticated() and user.is_superuser()
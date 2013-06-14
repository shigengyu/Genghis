from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.models import User
from social_auth.models import UserSocialAuth
from genghis.settings import ADMINS, GENGHIS_ENVIRONMENT

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
    authenticated = user.is_authenticated()
    is_superuser = user.is_superuser or GENGHIS_ENVIRONMENT == 'dev'
    return authenticated and is_superuser

def populate_is_superuser(request):
    user = request.user
    authenticated = hasattr(user, 'is_authenticated') and user.is_authenticated()
    is_superuser = authenticated and request.user.is_superuser
    if GENGHIS_ENVIRONMENT == 'dev':
        is_superuser = authenticated
    return {'is_superuser': is_superuser }

def populate_social_auth_backend(request):
    associated = None
    associated_name = None
    user = request.user
    if hasattr(user, 'is_authenticated') and user.is_authenticated():
        associated = UserSocialAuth.get_social_auth_for_user(user)
    if associated:
        for name in ['Google', 'Facebook', 'Linkedin', 'Flickr']:
            if name in str(associated):
                associated_name = name
                break;
    return {'associated_auth_backend': associated_name }
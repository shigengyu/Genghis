from django.views.generic.base import RedirectView

class WikiRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        return '/wiki/doku.php'

class MySqlRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        return '/mysql/index.php'

class WordPressRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        return '/wp'
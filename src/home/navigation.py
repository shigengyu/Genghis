def generate_navigation(request):
    url = request.get_full_path()
    return { 'url': url }

def generate_path_items(url):
    elements = url.split('/')
    path_items = []
    for e in elements:
        pass

url_name_mapping = {
                    'articles', 'Articles'
                    'tags', 'Tags'
                    }
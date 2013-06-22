def generate_navigation(request):
    url = request.get_full_path()
    return { 'url': url }

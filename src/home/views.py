# Create your views here.
from datetime import datetime
from django.shortcuts import render

def index(request):
    now = datetime.now()
    return render(request, 'index.html', {'current_date': now})
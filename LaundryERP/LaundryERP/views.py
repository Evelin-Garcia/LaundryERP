from django.shortcuts import render

def index(request):
    return render(request, 'index.html')#renderiza la plantilla index.html

def mi_error_403(request, exception=None):
    return render(request, '403.html', status=403)
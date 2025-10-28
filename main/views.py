from django.shortcuts import render

def list(request):
    return render(request, 'page-index-1.html')
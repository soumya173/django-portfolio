from django.shortcuts import render
from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'index.html', context)
def resume(request):
    context = {}
    return render(request, 'resume.html', context)

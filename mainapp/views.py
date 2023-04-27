from django.shortcuts import render

# Create your views here.

def blogPost(request):
    return render(request,'mainapp/index.html')
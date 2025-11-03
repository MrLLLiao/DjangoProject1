from django.shortcuts import render

def homepage(request):
    context = {'content':'<h1>欢迎来到我的网站</h1>'}
    return render(request, 'main.html', context);
from django.shortcuts import render, redirect

from login.models import Siteuser


# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')
# def login(request):
#     pass
#     return render(request, 'login/login.html')
def logout(request):
    if request.session.get('is_login'):
        request.session.flush()
    return redirect('/login/')
    # return render(request, 'login/logout.html')
def register(request):
    pass
    return render(request, 'login/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get(('username').strip())
        password = request.POST.get(('password').strip())
        print(username, password)
        if username and password:
            user = Siteuser.objects.filter(username=username, password=password)
            if user:
                request.session['is_login'] = True
                request.session['user_id'] = user.first().id
                request.session['username'] = user.first().username
                return redirect('/index')
            else:
                message = "Wrong username or password."
                return render(request, 'login/login.html', {'message': message})
        else:
            message = "Invalid username or password."
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')
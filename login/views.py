from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from login.models import Siteuser
from login.utils import login_required

# Create your views here.
def index(request):
    if request.session.get('is_login'):
        return redirect('/main/')
    return render(request, 'login/index.html')


# def login(request):
#     pass
#     return render(request, 'login/login.html')
def logout(request):
    if request.session.get('is_login'):
        request.session.flush()
    return render(request, 'login/index.html')
    # return render(request, 'login/logout.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get(('username').strip())
        password = request.POST.get(('password').strip())
        repassword = request.POST.get(('repassword').strip())
        email = request.POST.get(('email').strip())
        if not all([username, password, repassword, email]):
            return render(request, 'login/register.html', {'message': 'You should input all the information.'})
        if password != repassword:
            return render(request, 'login/register.html', {'message': 'Passwords should match.'})
        if Siteuser.objects.filter(username=username).exists():
            return render(request, 'login/login.html', {'message': 'Username already exists.'})
        if Siteuser.objects.filter(email=email).exists():
            return render(request, 'login/register.html', {"message": "Email already exists."})
        user = Siteuser.objects.create(username=username, password=make_password(password), email=email)
        request.session['is_login'] = True
        request.session['user_id'] = user.id
        request.session['username'] = username

        return redirect('/main/')
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

def main(request):
    username = request.session.get('username')
    return render(request, 'main.html', {'username': username})
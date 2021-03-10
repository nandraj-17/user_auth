from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
'''
def hi(request):
    return render(request,'MYAPPPRO/hi.html')
    #return HttpResponse('<h1>this is my 1st page</h1>')
'''
#signup view function
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'MYAPPPRO/signup.html', {'form':fm})

#Login view function
def index(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully!!')
                    return HttpResponseRedirect('/picture/')
                   # return HttpResponseRedirect('/profile/')

        else:
            fm = AuthenticationForm()
        return render(request, 'MYAPPPRO/index.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


#profile view function
def user_profile(request):
    if request.user.is_authenticated:
       return render(request, 'MYAPPPRO/profile.html', {'name': request.user})
       return HttpResponseRedirect('/profile/')
       #return render(request, 'MYAPPPRO/pictures.html')
      # return HttpResponseRedirect(request, 'MYAPPPRO/pictures.html')

    else:
        return HttpResponseRedirect('/login/')
#cookies

def picture(request):
    #picture(request)
    if request.user.is_authenticated:
        return render(request,'MYAPPPRO/pictures.html')

    else:
        return HttpResponseRedirect('/login/')
    #return HttpResponseRedirect('/profile/')

#logout view function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def setsession(request):
    request.index.session['uname'] = 'user'
    return render(request, '/profile/')

def getsession(request):
    # name = request.session['name']
    name = request.index.session.get('uname')
    return render(request, '/profile/', {'uname': name})



from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


# Create your views here.

def signin(request):
    '''
    User signin logic implemented using single function
    '''
    url = request.GET.get('next', '/')

    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(url)
        else:
            error = 'Login Failed'

    return render(request, 'accounts/signin.html', {'error':error})


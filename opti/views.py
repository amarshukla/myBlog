from django.shortcuts import render, render_to_response
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
c = {}

def login_user(request):
    c.update(csrf(request))
    return render_to_response('opti/loginView.html', c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/opti/loggedin')
    else:
        return HttpResponseRedirect('/opti/invalid')

def loggedin(request):
    return render_to_response('opti/loggedin.html',
                                {'full_name': request.user.username})

def logout(request):
    auth.logout(request)
    return render_to_response('opti/logout.html')

def invalidLogin(request):
    return render_to_response('opti/invalidLogin.html')

def list_dataset(request):
    return render(request, 'opti/listDataset.html')

def registerUser(request):
    #c.update(csrf(request))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/opti/registerSuccess') 
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    print args
    return render_to_response('opti/register.html',args)
    #return render_to_response('opti/registerUser.html',c)

def registerSuccess(request):
    
    return render_to_response('opti/registerSuccess.html')
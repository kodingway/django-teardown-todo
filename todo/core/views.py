from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Todo

# Create your views here.

@login_required(login_url='/accounts/signin/')
def home(request):
    '''
    default page for app&prj
    '''
    return render(request, 'base.html')


@login_required(login_url='accounts/signin/')
def list_view(request):
    '''
    Todo list view
    '''
    todo_list = get_list_or_404(Todo, owner=request.user)
    return render(request, 'core/todo_list.html', {'todo_list':todo_list})

@login_required(login_url='accounts/signin/')
def add_view(request):
    '''
    Add todo item view
    '''
    if request.method == 'POST':
        content = request.POST['content']
        owner = request.user
        td = Todo(content=content, owner=owner)
        try:
            td.save()
            return HttpResponseRedirect(reverse('todo-list'))
        except IntegrityError:
            return render(request, 'core/todo_form.html', {'content':content})
    else:
        return render(request, 'core/todo_form.html')

@login_required(login_url='accounts/signin/')
def edit_view(request, tid):
    '''
    Edit todo item view
    '''
    todo = get_object_or_404(Todo, pk=tid)

    if request.method == 'POST':
        todo.content = request.POST.get('content','')
        todo.status = request.POST.get('status',False)
        try:
            todo.save()
            return HttpResponseRedirect(reverse('todo-list'))
        except IntegrityError:
            return render(request, 'core/todo_form.html', {'content':todo.content, 'status':todo.status})
    else:
        return render(request, 'core/todo_form.html', {'content':todo.content, 'status':todo.status})

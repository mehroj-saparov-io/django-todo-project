from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(user=request.user, title=title)
            return redirect('todo-list')

    return render(request, 'todos/todo_create.html')

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todo-list')

    return render(request, 'todos/todo_update.html', {'todo': todo})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect('todo-list')

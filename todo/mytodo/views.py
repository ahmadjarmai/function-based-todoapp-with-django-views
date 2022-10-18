from django.shortcuts import get_object_or_404, redirect, render

from mytodo.forms import TodoForm
from .models import Todo

def List(request) :
    todos =Todo.objects.all()
    return render(request, 'myapp/list.html', {'todos' :todos})

def Detail(request, todo_id) :
    todo =get_object_or_404(Todo, id =todo_id)
    return render(request, 'myapp/detail.html', {'todo' :todo})

def Update(request, todo_id) :
    todo =get_object_or_404(Todo, id=todo_id)
    if request.method =='POST' :
        form =TodoForm(instance=todo, data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect('detail', todo_id=todo.id)

    return render(request, 'myapp/update.html', {'form' : TodoForm(instance=todo)})

def Create(request) :
    if request.method =="POST" :
        form =TodoForm(data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect('list')

    return render(request, 'myapp/create.html', {'form' :TodoForm})

def Delete(request, todo_id) :
    todo =get_object_or_404(Todo, id =todo_id)
    if request.method =='POST' :
        todo.delete()
        return redirect('list')

    return render(request, 'myapp/delete.html')


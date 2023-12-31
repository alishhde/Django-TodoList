from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task


def index_view(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    tasks = Task.objects.all()

    context = {
        'form': form,
        'tasks': tasks,
    }

    return render(request, 'index.html', context)


def update_task_view(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "task_edit_form": form,
    }

    return render(request, "update_task.html", context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")

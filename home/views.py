from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from home.models import Task



#   count =0;
# # Create your views here.
# def inddex(request):
  
#     
#     for task in tasks:
#         count = count+1

def add_task(request):
    try:
        context = {'success':1}
        
        context = {'success':1}
        if request.method == "POST":
            title = request.POST['title']
            desc = request.POST['desc']
            ins = Task(taskName = title,taskDesc = desc)
            t = title

            if t.strip():
                ins.save()
                context = {'success':2}
            else:
                context = {'success':3}

        return render(request, "home/add_task.html",context)
    except:
        return redirect('add_task')

def task(request):
    try:
        allTasks = Task.objects.all()
        tasks = Task.objects.all()
        
        count=0
        for task in tasks:
            count = count+1
        context = {'tasks':allTasks,'status':count}
        return render(request, "home/tasks.html", context)
    except:
        redirect('add_task')

def delete(request,pk):
    try:
        obj = Task.objects.get(id=pk)
        if request.method == 'POST':
            obj.delete()
            return task(request)

        context = {'item' : obj}
        return render(request, "home/delete.html",context)
    except:
        return redirect('add_task')

def update(request, pk):
    try:
        item = Task.objects.get(id = pk)
        context = {'title': item.taskName, "desc": item.taskDesc,'success':1}
        if request.method == 'POST':
            x = item.taskName = request.POST['title']
            item.taskDesc = request.POST['desc']
            if x.strip():
                item.save()
                context = {'title': item.taskName, "desc": item.taskDesc,'success':2}
            else:
                context = {'title': item.taskName, "desc": item.taskDesc,'success':3}

        return render(request, "home/update_task.html",context)
    except:
        return redirect('tasks')


def view_task(request, pk):
    try:
        item = Task.objects.get(id=pk)
        context = {'title':item.taskName, "desc":item.taskDesc, "time":item.time, 'id':pk}
        return render(request, "home/view_task.html",context)

    except:
        return redirect('tasks')


def about(request):
    return render(request,"home/about.html")
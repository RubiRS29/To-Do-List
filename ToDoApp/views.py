from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from toDoTasks.forms import TaskForm
from formLists.forms import ListForm

from toDoTasks.utilities import count_task, all_task
from toDoTasks.models import Task


from user.models import User

import datetime


@login_required(login_url='/user/login_view')
def index(request):

    today = datetime.datetime.now()
    tomorrow = today + datetime.timedelta(days=1)

    form_task = TaskForm( request.POST or None )
    form_list = ListForm( request.POST or None )
    user = request.user
    gretting = User.get_gretting( user ) 

    count_task = all_task(user , today).count()
    task_today = all_task(user , today)
    

    allTask = all_task( user , tomorrow)


    if request.method == 'POST' and form_task.is_valid():
        formTask = form_task.save( commit=False )       
        formTask.user = user
        formTask.save()
        return redirect('http://127.0.0.1:8000/ToDoList/')

    elif request.method == 'POST' and form_list.is_valid():
        formList = form_list.save( commit=False )
        formList.user = user
        formList.save()
        return redirect('http://127.0.0.1:8000/ToDoList/')

    else:
        pass

    return render (request , 'layout_app.html', {
        'form_task': form_task, 
        'form_list': form_list, 
        'gretting' : gretting,
        'countTask' : count_task,
        'task_today' : task_today,
        'all_task' : allTask,
        
    })
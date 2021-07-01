from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from django.http import HttpResponse, HttpResponseRedirect


from toDoTasks.forms import TaskForm
from formLists.forms import ListForm
from toDoTasks.models import Task
from formLists.models import List
from toDoTasks.utilities import count_task, all_task
from formLists.utils import get_all_list
from user.models import User

from .utils  import create_task_or_list


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

    create_task_or_list(request , form_task , form_list , user )

    return render (request , 'index_app.html', {
        'form_task': form_task, 
        'form_list': form_list, 
        'gretting' : gretting,
        'countTask' : count_task,
        'my_list_or_task' : task_today,
        'all_task' : allTask,  
        "text_info" : "Here your tasks for today",
    })


@login_required(login_url='/user/login_view')
def ListView(request):
    form_task = TaskForm( request.POST or None )
    form_list = ListForm( request.POST or None )
    user = request.user

    my_list = get_all_list(user)
    print(my_list)
   
    
    gretting = "Holi {}".format(user.username)
    

    create_task_or_list(request , form_task , form_list , user )

    return render (request , 'list_app.html', {
        'form_task': form_task, 
        'form_list': form_list, 
        'gretting' : gretting,  
        'my_list_or_task' : my_list,  
        # 'countTask' : my_lists_count, 
        "text_info" : "Here your tasks",
    })

@login_required(login_url='/user/login_view')
def schedule_View(request):
    form_task = TaskForm( request.POST or None )
    form_list = ListForm( request.POST or None )
    user = request.user
    count_task = all_task(user.id ).count()
    
    gretting = "Hello {}".format(user.username)
    allTask = all_task( user )

    create_task_or_list(request , form_task , form_list , user )

    return render (request , 'schedule.html', {
        'form_task': form_task, 
        'form_list': form_list, 
        'gretting' : gretting,
        'my_list_or_task' : allTask,  
        'countTask' : count_task, 
        "text_info" : "Here your tasks",
    })


def DeleteTask(request , id ):

    task = Task.objects.get(id=id)
    task.delete()
    #esta linea hace que la persona regrese a la misma url 
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


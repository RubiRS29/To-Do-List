from django.shortcuts import redirect

def create_task_or_list(request , form_task , form_list , user ):

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


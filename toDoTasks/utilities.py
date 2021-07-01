from .models import Task
import datetime

def count_task(id_user):
    taskCount = Task.objects.filter(user=id_user).count()
    return taskCount


def all_task(id_user , date  = None ):
    if date is None:
        task_today = Task.objects.filter(user=id_user).order_by('date')
    else:
        task_today = Task.objects.filter(user=id_user , date=date).order_by('date')
    return task_today
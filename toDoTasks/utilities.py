from .models import Task
import datetime

def count_task(id_user):
    taskCount = Task.objects.filter(user=id_user).count()
    return taskCount


def all_task(id_user , date ):
    task_today = Task.objects.filter(user=id_user , date=date).order_by('date')
    return task_today
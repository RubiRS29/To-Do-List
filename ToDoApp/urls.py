from django.urls import path

from .views import index, ListView , schedule_View , DeleteTask

app_name = 'to-do-app'

urlpatterns = [
    # ... snip ...
    path('' , index , name='ToDoList'),
    path('Lists' , ListView , name='list_app'),
    path('Schedule' , schedule_View , name='schedule_app'),
    path('<int:id>' , DeleteTask , name='delete'),
    path('Lists/<int:id>' , DeleteTask , name='delete'),
    path('Schedule/<int:id>' , DeleteTask , name='delete'),
    
]
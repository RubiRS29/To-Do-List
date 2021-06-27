from django.urls import path

from .import views

app_name = 'to-do-app'

urlpatterns = [
    # ... snip ...
    path('' , views.index , name='ToDoList'),
    # path('login_view' , views.login_view , name='login_view'),
    # path('logout_view' , views.logout_view , name='logout_view'),
    
]
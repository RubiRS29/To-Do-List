from django.db import models

from user.models import User

from formLists.models import List
class Task(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField( max_length=150 )
    date = models.DateField()
    listAdd = models.ForeignKey(List , verbose_name=("Lists") , on_delete=models.CASCADE , null=True , default=None )
    create_at = models.DateField( auto_now_add=True )

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return self.title
    
    
    

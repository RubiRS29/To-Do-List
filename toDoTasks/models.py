from django.db import models

from user.models import User

class Task(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField( max_length=150 )
    date = models.DateField()
    listAdd = models.CharField( max_length=100 , default=None , blank=True, null=True)
    create_at = models.DateField( auto_now_add=True )

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return self.title

    

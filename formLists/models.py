from django.db import models

from user.models import User


class List(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    create_at = models.DateField( auto_now_add=True )

    class Meta:
        verbose_name = ("List")
        verbose_name_plural = ("Lists")

    def __str__(self):
        return self.title


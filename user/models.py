from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals  import pre_save

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField( max_length=150 , unique=False , null=True , blank = True )
    pic_choice = models.IntegerField(default=1 , verbose_name='pic_choice')
    email = models.CharField( max_length=255,  unique=True )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

    objects = MyUserManager()

    def get_gretting(self):
        return "Welcome back, {}!".format(self.username)



# def username_default( sender , instance , *args, **kwargs):
#     if instance.username == None:
#         user_name = "{}-{}".format(instance.first_name , instance.last_name[:2])
    
#     instance.username = user_name

# pre_save.connect( username_default , sender=User )       
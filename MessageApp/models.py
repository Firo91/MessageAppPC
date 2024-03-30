from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, full_name, title, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, full_name=full_name, title=title, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, full_name, title, password=None, **extra_fields):
        user = self.create_user(username, full_name, title, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'title']

    def __str__(self):
        return self.username

class MyMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    background_color = models.CharField(max_length=20, blank=True, null=True, choices=[('green', 'Green'), ('red', 'Red'), ('yellow', 'Yellow'),('#A91101', 'Soft Red'),('', 'No Color')])
    status = models.CharField(max_length=20,blank=True, null=True, choices=[('Ledig', 'Ledig'), ('Møte', 'Møte'), ('Ikke på kontoret', 'Ikke på kontoret'),('På Reise','På Reise'),('På Terminalen','På Terminalen'),('','No Status')], default='')
    background_image = models.CharField(max_length=255, blank=True, null=True, choices=[('flyingPlan.mp4', 'Reise'),('Matrix.mp4', 'Kontoret'),('meeting.mp4', 'Møte'),('terminal.mp4', 'Terminal')])

from django.db import models

# Create your models here.

from django.db import models

class Siteuser(models.Model):
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    username = models.CharField(max_length = 128, unique = True, verbose_name = 'Username')

    password = models.CharField(max_length = 100, unique = True, verbose_name = 'Password')

    email = models.EmailField(unique = True, verbose_name = 'Email')

    gender = models.CharField(default = 0, choices = gender_choice, verbose_name = 'Gender')

    creat_time = models.DateTimeField(auto_now_add = True, verbose_name = 'Creation Time')
    modify_time = models.DateTimeField(auto_now = True, verbose_name = 'Modify Time')

    last_login_time = models.DateTimeField(null = True, blank = True, verbose_name = 'Last Login Time')

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'siteuser'
        verbose_name = 'Site User'
        verbose_name_plural = 'Site Users'
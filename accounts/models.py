from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    ROLE = (
        ('Администратор', 'Администратор'),
        ('Студент', 'Студент'),
        ('Преподаватель', 'Преподаватель')
    )

    username = models.CharField(unique=True, default='', max_length=100, verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name='Эл. адрес')
    role = models.CharField(max_length=100, choices=ROLE, default='Студент', verbose_name='Роль')

    firstname = models.CharField(max_length=100, default='', verbose_name='Имя')
    surname = models.CharField(max_length=100, default='', verbose_name='Фамилия')
    lastname = models.CharField(max_length=100, default='', verbose_name='Отчество')

    work_groups = models.ManyToManyField('core.WorkGroup', related_name='user_groups', blank=True)

    def __str__(self):
        return self.fn()

    def fn(self):
        return f"{self.surname} {self.firstname} {self.lastname}"

    def is_student(self):
        return self.role == 'Студент'

    def is_tutor(self):
        return self.role == 'Преподаватель'

    def is_admin(self):
        return self.role == 'Администратор'

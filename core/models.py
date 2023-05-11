from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

from accounts.models import User


# Create your models here.
class WorkDay(models.Model):
    DAY = (
        ('ПН', 'Понедельник'),
        ('ВТ', 'Вторник'),
        ('СР', 'Среда'),
        ('ЧТ', 'Четверг'),
        ('ПТ', 'Пятница'),
        ('СБ', 'Суббота'),
        ('ВС', 'Воскресенье'),
    )
    day = models.CharField(max_length=10, choices=DAY)

    def __str__(self):
        return self.day


class Department(models.Model):
    depTitle = models.CharField(max_length=150, unique=True)
    groupPrice = models.IntegerField()
    indPrice = models.IntegerField()

    def __str__(self):
        return self.depTitle


class WorkGroupPost(models.Model):
    TYPE = (
        ('Сообщение', 'Сообщение'),
        ('Важно', 'Важно')
    )

    postTag = models.CharField(max_length=100, choices=TYPE)
    postTitle = models.CharField(max_length=200)
    postBody = models.TextField()
    postCreationDate = models.DateTimeField(auto_now_add=True)


class WorkGroup(models.Model):
    TYPE = (
        ('Групповые занятия', 'Групповые занятия'),
        ('Индивидуальные занятия', 'Индивидуальные занятия')
    )
    groupName = models.CharField(max_length=100, unique=True)
    groupType = models.CharField(max_length=100, choices=TYPE, default=TYPE[0])
    groupDep = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    groupTeacher = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    groupDays = models.ManyToManyField(WorkDay, related_name='group_days')
    groupStudents = models.ManyToManyField(User, related_name='group_students', blank=True)
    groupTime = models.CharField(max_length=1000, default='', blank=True)
    groupPosts = models.ManyToManyField(WorkGroupPost, related_name='group_posts')

    def get_absolute_url(self):
        return reverse('groupDetail', kwargs={'pk': self.pk})

    def add_student(self, student:User):
        if student.is_student():
            self.groupStudents.add(student)
            student.work_groups.add(self)

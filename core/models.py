from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
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
    class Meta:
        ordering = ['-postCreationDate']

    TYPE = (
        ('Сообщение', 'Сообщение'),
        ('Важно', 'Важно'),
        ('Домашнее задание', 'Домашнее задание')
    )

    postTag = models.CharField(max_length=100, choices=TYPE)
    postTitle = models.CharField(max_length=200)
    postBody = models.TextField()
    postCreationDate = models.DateTimeField(auto_now_add=True)


class GroupHomeTask(models.Model):
    class Meta:
        ordering = ['-taskDate']

    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    taskDate = models.DateTimeField(auto_now_add=True)
    taskDeadline = models.DateTimeField()
    taskFile = models.FileField(upload_to='hometaskfiles/', blank=True, null=True)
    taskSolutions = models.ManyToManyField('GroupTaskSolution', blank=True, null=True)

    def add_to_group(self, group):
        group.groupHometasks.add(self)

    def __str__(self):
        return self.taskTitle


class GroupTaskSolution(models.Model):
    solutionFrom = models.ForeignKey('accounts.User', related_name='solution_from', on_delete=models.CASCADE)
    solutionFile = models.FileField(upload_to='tasksolutions/')
    solutionForTask = models.ForeignKey('GroupHomeTask', related_name='solution_for_task', on_delete=models.CASCADE)
    solutionDatetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def add_to_task(self):
        print(self.solutionForTask)
        self.solutionForTask.taskSolutions.add(self)


class Mark(models.Model):
    markForUser = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    markValue = models.IntegerField(default=0, validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ])
    markTarget = models.CharField(max_length=500)
    markGroup = models.ForeignKey('WorkGroup', on_delete=models.CASCADE)
    markComment = models.CharField(max_length=1000)
    markConnectedTask = models.ForeignKey('GroupHomeTask', on_delete=models.CASCADE, blank=True)


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
    groupHometasks = models.ManyToManyField(GroupHomeTask, related_name='groups_tasks')

    def get_absolute_url(self):
        return reverse('groupDetail', kwargs={'pk': self.pk})

    def add_student(self, student: User):
        if student.is_student():
            self.groupStudents.add(student)
            student.work_groups.add(self)

    def __str__(self):
        return self.groupName
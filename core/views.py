from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, CreateView
import core.tools.notifyme as notify

from accounts.models import User
from .models import WorkGroup, GroupHomeTask, GroupTaskSolution, Mark
from .forms import NewGroupForm, AddStudentToGroupForm, AddGroupPost, CreateTaskForGroup, SendTaskSolution, SetMarkToStudent
from django.contrib.auth import views, forms, authenticate, login, logout
from accounts.forms import NewUserForm

from django.core.mail import send_mail


def admin_only(func):
    def check(request):
        if request.user.is_admin():
            return func(request)
        else:
            return redirect('personal')

    return check


def inner_only(func):
    def check(request, pk):
        group = WorkGroup.objects.get(pk=pk)
        if request.user.is_admin() or request.user in group.groupStudents.all() or group.groupTeacher == request.user:
            return func(request, pk)
        else:
            return redirect('noPermForGroup')

    return check


# Create your views here.

class Index(View):
    template_name = 'pages/index.html'

    def get(self, request):
        form = forms.AuthenticationForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = forms.AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
        return render(request, self.template_name, context={'form': form})


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required(login_url='')
def personal(request):
    return render(request, 'personal.html', {})


@login_required(login_url='')
@admin_only
def users_list(request):
    context = {}
    context['users_list'] = User.objects.all()
    return render(request, 'pages/admin/users_list.html', context)


@login_required(login_url='')
@admin_only
def groups_list(request):
    context = {}
    context['groups_list'] = WorkGroup.objects.all()
    return render(request, 'pages/admin/groups_list.html', context)


@login_required(login_url='')
@admin_only
def create_user(request):
    context = {}
    context['form'] = NewUserForm(request.POST or None)
    if request.method == "POST":
        print('sdfsfd')
        form = NewUserForm(request.POST)
        if form.is_valid():
            r = form.save()
            r.set_password(form.cleaned_data['password'])
            r.save()
            messageEmail = f'<p>Здравствуйте! Вы были зарегистрированы на платформе My.TLearn.</p>' \
                           f'<p>Ваш логин: {form.cleaned_data["username"]}</p>' \
                           f'<p>Ваш пароль: {form.cleaned_data["password"]}</p>' \
                           f'<p>Желаем приятной и продуктивной учебы!</p>'
            send_mail(
                subject='Добро пожаловать в TLearn!',
                message=messageEmail,
                html_message=messageEmail,
                from_email='support@tlearn.ru',
                recipient_list=[form.cleaned_data["email"]],
                fail_silently=False
            )
            return redirect('users')
    return render(request, 'pages/admin/create_user.html', context)


@login_required(login_url='')
@admin_only
def create_group(request):
    context = {}
    form = NewGroupForm(request.POST or None)
    form.fields['groupTeacher'].queryset = User.objects.filter(role='Преподаватель')
    context['form'] = form
    if request.method == "POST":
        print('sdfsfd')
        form = NewGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    return render(request, 'pages/admin/create_group.html', context)


@login_required(login_url='')
@inner_only
def group_detail(request, pk):
    group = WorkGroup.objects.get(pk=pk)
    context = {'group': WorkGroup.objects.get(pk=pk)}
    if request.user.is_admin():
        addStudentForm = AddStudentToGroupForm(request.POST or None)
        context['addUserForm'] = addStudentForm
        if addStudentForm.is_valid():
            WorkGroup.objects.get(pk=pk).add_student(addStudentForm.cleaned_data['student'])
            context = notify.AddNotifyToQueue(context, 'Студент добавлен',
                                              f"{addStudentForm.cleaned_data['student']} успешно добавлен в группу {WorkGroup.objects.get(pk=pk)}")

    if request.user.is_tutor() or request.user.is_admin():
        print(request.FILES)
        createTaskForm = CreateTaskForGroup(request.POST or None, request.FILES)
        context['createTaskForm'] = createTaskForm
        if createTaskForm.is_valid():
            t = createTaskForm.save()
            t.add_to_group(group)
        createPostForm = AddGroupPost(request.POST or None)
        context['createPostForm'] = createPostForm
        if createPostForm.is_valid():
            post = createPostForm.SavePost()
            group.groupPosts.add(post)

    if request.user.is_student():
        sendTaskSolutionForm = SendTaskSolution(request.POST or None, request.FILES)
        context['sendTaskSolutionForm'] = sendTaskSolutionForm
        print('PROCESSING')
        if sendTaskSolutionForm.is_valid():
            s = sendTaskSolutionForm.save()
            s.add_to_task()
            print('ACCEPTED')
            messageEmail = f'<p>Студент {request.user} из группы {group.groupName} отправил решение домашнего задания "{s.solutionForTask}".</p>'
            send_mail(
                subject=f'{request.user} прислал решение',
                message=messageEmail,
                html_message=messageEmail,
                from_email='support@tlearn.ru',
                recipient_list=[group.groupTeacher.email],
                fail_silently=False
            )
        else:
            print(sendTaskSolutionForm.errors)

        context['solutions'] = GroupTaskSolution.objects.filter(solutionFrom=request.user)

    if request.user.is_tutor():
        addMarkForm = SetMarkToStudent(request.POST or None)
        context['solutions'] = GroupTaskSolution.objects.filter(solutionForTask__in=group.groupHometasks.all())

    return render(request, 'pages/general/group_detail.html', context)


@login_required(login_url='')
def student_groups(request):
    context = {}
    context['groups'] = request.user.work_groups.all()
    return render(request, 'pages/student/student_groups.html', context)


@login_required(login_url='')
def tutor_groups(request):
    context = {}
    context['groups'] = WorkGroup.objects.filter(groupTeacher=request.user)
    return render(request, 'pages/tutor/tutor_groups.html', context)


def group_no_perm(request):
    return render(request, 'pages/general/no_perm_to_group.html', {})


def students_marks(request):
    context = {}
    context['groups'] = request.user.work_groups.all()
    context['marks'] = {}
    for group in list(context['groups']):
        context['marks'][group.groupName] = Mark.objects.filter(markForUser=request.user, markGroup=group)

    return render(request, 'pages/student/students_marks.html', context)
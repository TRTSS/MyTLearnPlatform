from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('my/', personal, name='personal'),
    path('my/users', users_list, name='users'),
    path('logout/', logout_user, name='logout'),
    path('my/users/create', create_user, name='userCreate'),
    path('my/groups', groups_list, name='groups'),
    path('my/groups/create', create_group, name='groupCreate'),
    path('my/group/<int:pk>', group_detail, name='groupDetail'),
    path('my/group/blocked', group_no_perm, name='noPermForGroup'),
    path('my/studentgroups', student_groups, name='studentGroups'),
    path('my/tutorgroups', tutor_groups, name='tutorGroups'),
    path('my/studentmarks', students_marks, name='studentMarks')
]

from django import template
from core.models import WorkGroup, WorkGroupPost, GroupHomeTask, Mark
from core.forms import SetMarkToStudent
from typing import List

register = template.Library()


@register.inclusion_tag('widgets/group_schedule.html', name='schedule')
def schedule(group: WorkGroup):
    days = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
    gDays = [x.day for x in list(group.groupDays.all())]
    t = group.groupTime.split()
    print(t)
    gTimes = []
    for d in days:
        if d in gDays:
            gTimes.append(t.pop(0))
        else:
            gTimes.append('-')
    res = [(x in gDays) for x in days]
    print(res)
    return {
        'days': res,
        'times': gTimes
    }


@register.inclusion_tag('widgets/group_schedule_mini.html', name='schedule_mini')
def schedule_mini(group: WorkGroup):
    days = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
    gDays = [x.day for x in list(group.groupDays.all())]
    t = group.groupTime.split()
    print(t)
    gTimes = []
    for d in days:
        if d in gDays:
            gTimes.append(t.pop(0))
        else:
            gTimes.append('-')
    res = [(x in gDays) for x in days]
    print(res)
    return {
        'days': res,
        'times': gTimes
    }


@register.inclusion_tag('widgets/group_post.html', name='postdecor')
def postdecor(post: WorkGroupPost):
    return {
        'post': post,
        'type': post.postTag
    }


@register.inclusion_tag('widgets/group_task.html', name='taskdecor', takes_context=True)
def taskdecor(context, task: GroupHomeTask):
    data = {
        'task': task,
        'request': context['request']
    }
    if context['request'].user.is_student():
        data['sendTaskSolutionForm'] = context['sendTaskSolutionForm']
        data['solutions'] = context['solutions'].filter(solutionForTask=task)
    if context['request'].user.is_tutor():
        data['solutions'] = context['solutions'].filter(solutionForTask=task)
        addMarkForTask = SetMarkToStudent(initial={
            'markConnectedTask': task,
            'markGroup': context['group']
        })
        addMarkForTask.fields['markConnectedTask'].widget.attrs['readonly'] = True
        data['addMarkForm'] = addMarkForTask
    return data


class Marks:
    pass


@register.inclusion_tag('widgets/group_marks_student.html', name='groupmarks', takes_context=True)
def groupmarks(context, group: WorkGroup):
    marks = Mark.objects.filter(markForUser=context['request'].user, markGroup=group)
    data = {
        'marks': marks,
        'group': group,
        'request': context['request']
    }
    return data

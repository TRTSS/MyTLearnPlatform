from django import template
from core.models import WorkGroup, WorkGroupPost

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

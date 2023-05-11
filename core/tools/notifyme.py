def AddNotifyToQueue(context: dict, title, message):
    if 'notifications' not in context.keys():
        context['notifications'] = []
    context['notifications'].append((title, message))
    return context

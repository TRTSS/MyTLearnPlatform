from django import forms
from .models import WorkGroup, WorkGroupPost
from accounts.models import User


class NewGroupForm(forms.ModelForm):
    class Meta:
        model = WorkGroup
        fields = ['groupName', 'groupDep', 'groupType', 'groupTeacher', 'groupDays', 'groupTime']


class AddStudentToGroupForm(forms.Form):
    student = forms.ModelChoiceField(User.objects.filter(role='Студент'))


class AddGroupPost(forms.Form):
    type = forms.ChoiceField(choices=WorkGroupPost.TYPE)
    title = forms.CharField(max_length=200)
    body = forms.CharField(max_length=1000, widget=forms.Textarea)

    def SavePost(self):
        data = self.cleaned_data;
        post = WorkGroupPost(postTag=data['type'], postTitle=data['title'], postBody=data['body'])
        post.save()
        return post

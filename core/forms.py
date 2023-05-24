from django import forms
from .models import WorkGroup, WorkGroupPost, GroupHomeTask, GroupTaskSolution, Mark
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


class CreateTaskForGroup(forms.ModelForm):
    class Meta:
        model = GroupHomeTask
        fields = ['taskTitle', 'taskDescription', 'taskDeadline', 'taskFile']
        widgets = {
            'taskDeadline': forms.DateTimeInput()
        }


class SendTaskSolution(forms.ModelForm):
    class Meta:
        model = GroupTaskSolution
        fields = ['solutionFrom', 'solutionFile', 'solutionForTask']
        widgets = {
            'solutionFrom': forms.HiddenInput(),
            'solutionForTask': forms.HiddenInput()
        }


class DeleteTaskForm(forms.ModelForm):
    class Meta:
        model = GroupHomeTask
        fields = ['id']


class SetMarkToStudent(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['markForUser', 'markGroup', 'markConnectedTask', 'markValue', 'markTarget', 'markComment']
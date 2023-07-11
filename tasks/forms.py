from django import forms
from django.forms import CheckboxSelectMultiple

from tasks.models import Task, Worker


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        input_formats=["%Y-%m-%dT%H:%M"]
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.exclude(is_superuser=True),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = Task
        exclude = ["created_by", "updated_by"]

    def save(self, commit=True, created_by=None, updated_by=None):
        instance = super().save(commit=False)
        if created_by:
            instance.created_by = created_by
        if updated_by:
            instance.updated_by = updated_by
        if commit:
            instance.save()
            self.save_m2m()
        return instance

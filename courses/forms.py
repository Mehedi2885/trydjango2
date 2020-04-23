from django import forms
from .models import Courses


class CourseModelForms(forms.ModelForm):
    class Meta:
        model = Courses
        fields = [
            'title'
        ]

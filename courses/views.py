from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Courses


# Create your views here.

# BASE VIEW Class = View
class CourseView(View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
            context = {'object': obj}
        return render(request, self.template_name, context)


# HTTP Method

def my_fbv(request, *args, **kwargs):
    return render(request, "about.html", {})

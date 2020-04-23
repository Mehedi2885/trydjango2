from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Courses
from .forms import CourseModelForms


# Create your views here.

# BASE VIEW Class = View

class CourseViewMixin(object):
    model = Courses

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
        return obj


class CourseDeleteView(CourseViewMixin, View):
    template_name = 'courses/course_delete.html'

    # GET method for create form
    def get(self, request, id=None,  *args, **kwargs, ):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    # POST method for create form
    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)


class CourseUpdateView(CourseViewMixin, View):
    template_name = 'courses/course_update.html'
    form = CourseModelForms()

    # GET method for create form
    def get(self, request, id=None,  *args, **kwargs, ):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForms(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    # POST method for create form
    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForms(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                form = self.form
                context['object'] = obj
                context['form'] = form
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    form = CourseModelForms()

    # GET method for create form
    def get(self, request, *args, **kwargs):
        context = {"form": self.form}
        return render(request, self.template_name, context)

    # POST method for create form
    def post(self, request, *args, **kwargs):
        form = CourseModelForms(request.POST)
        if form.is_valid():
            form.save()
            form = self.form
        context = {'form': form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Courses.objects.all()

    def get(self, request, *args, **kwargs):
        context = {"object_list": self.queryset}
        return render(request, self.template_name, context)


class CourseView(CourseViewMixin, View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        if id is not None:
            obj = self.get_object() # get_object_or_404(Courses, id=id)
            context = {'object': obj}
        return render(request, self.template_name, context)


# HTTP Method

def my_fbv(request, *args, **kwargs):
    return render(request, "about.html", {})

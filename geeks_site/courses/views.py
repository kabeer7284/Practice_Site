from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Subject
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


class AboutUs(TemplateView):
    template_name = 'courses/about.html'


class CoursesList(ListView):
    # specify the model for list view
    model = Course
    template_name = "courses/about.html"

    def get_queryset(self, *args, **kwargs):
        qs = Course.objects.all().count()
        print(qs, "---------------------------------------------------------------")

        return Course.objects.all()


class CoursesCreate(CreateView):
    model = Course
    template_name = "courses/create_courses.html"
    fields = ['name', 'description', 'price', 'start_date', 'end_date']

# def first_view(request):
#   if request.method == "GET":
#       return HttpResponse("This is simple result")
#   elif request.method == "Post":
#       pass

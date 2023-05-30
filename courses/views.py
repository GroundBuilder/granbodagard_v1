from django.shortcuts import render

from .models import Course, Category

# Create your views here.

def all_courses(request):
    """ A view to show all products, including sorting and search queries. """

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)
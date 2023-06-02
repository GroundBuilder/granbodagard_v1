from django.shortcuts import render, get_object_or_404

from .models import Course, Category

# Create your views here.

def all_courses(request):
    """ A view to show all courses, including sorting and search queries. """

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)


def course_details(request, course_id):
    """ A view to show the course with details. """

    course = get_object_or_404(Corse, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_details.html', context)
from django.shortcuts import render
from .models import Course
from django.db.models import Q
# Create your views here.
def index(request):
 
    return render(request,'index.html')

def courses(request):
    course=Course.objects.all()
    return render(request,'course.html',{'course':course})


def search_courses(request):
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Course.objects.filter(Q(course_name__icontains=query) )

    return render(request, 'course.html', {'query': query, 'course': results})
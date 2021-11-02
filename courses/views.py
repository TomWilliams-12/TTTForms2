from django.shortcuts import redirect, render
from django.views import View
from courses.forms import CourseForm
from courses.models import Courses
from datetime import datetime

class CreateCourse(View):
    def get(self, request):
        try:
            prev_cn = Courses.objects.last()
            int_cn = int(prev_cn.course_number)
            next_cn = int_cn + 1
        except:
            next_cn = None
        course_form = CourseForm(initial={'course_number': next_cn, 'instructor': request.user, 'venue': 'TTT', 'start_date': datetime.today()})
        return render(request, 'create_course.html', {'course_form': course_form })

    def post(self, request):
        course_form = CourseForm(request.POST)

        if course_form.is_valid():
            course_form.save()
            return redirect('/')



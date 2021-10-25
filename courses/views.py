from django.shortcuts import redirect, render
from django.views import View
from courses.forms import CourseForm
from accounts.models import Profile
from courses.models import Courses

class CreateCourse(View):
    
    def get(self, request):
        prev_cn = Courses.objects.last()
        int_cn = int(prev_cn.course_number)
        next_cn = int_cn + 1
        course_form = CourseForm(initial={'course_number': next_cn, 'instructor': request.user})
        return render(request, 'create_course.html', {'course_form': course_form })

    def post(self, request):
        course_form = CourseForm(request.POST)

        if course_form.is_valid():
            course_form.save()
            return redirect('/')

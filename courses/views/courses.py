from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect

from courses.models import Course,Video

def CoursePage(request,slug):
    print(slug)
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number = serial_number ,course = course)

    if((request.user.is_authenticated is False) and ( video.is_preview is False) ):
        return redirect('login')
    print(video)

    context = {
        "course" : course,
        "video" : video,
        "videos": videos
    }
    return render(request,template_name="courses/course_page.html",context=context)
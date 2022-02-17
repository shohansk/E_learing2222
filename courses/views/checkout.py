from multiprocessing import context
from venv import create
from django.http import HttpResponse
from django.shortcuts import render,redirect

from courses.models import Course,Video

def checkout(request,slug):
    course = Course.objects.get(slug = slug)


    if((request.user.is_authenticated is False)):
        return redirect('login')

    action = request.GET.get('action')
    order  = None
    if action == "create_payment":
        print("create Order pace")
        order = "order done"
    context = {
        "course" : course,
        "order" :order,
    }
    return render(request,template_name="courses/check_out.html",context=context)




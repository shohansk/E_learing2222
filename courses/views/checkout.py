from locale import currency
from multiprocessing import context
from venv import create
from django.http import HttpResponse
from django.shortcuts import render,redirect

from courses.models import Course,Video
from E_learing.settings import *
from datetime import datetime
from time import time

import razorpay
client = razorpay.Client(auth=(KEY_ID , KEY_SECRET))

def checkout(request,slug):
    course = Course.objects.get(slug = slug)


    if((request.user.is_authenticated is False)):
        return redirect('login')
    user = request.user
    action = request.GET.get('action')
    order  = None
    if action == "create_payment":
        amount = int((course.price- (course.price * course.discount * 0.01))*100)
        currency = 'BDT'
        notes = {
            "email" : user.email,
            "name" : f'{user.first_name} {user.last_name}'
        }
        receipt  = f"Abdul ALim Shohan -{int(time())}"
        order =  client.order.create({
            'receipt':receipt ,
             'notes': notes,
             'amount': amount,
             'currency': currency
             
             })
        
    context = {
        "course" : course,
        "order" :order
    }
    return render(request,template_name="courses/check_out.html",context=context)




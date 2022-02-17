from ast import Expression
from locale import currency
from multiprocessing import context
from venv import create
from xml.dom.minidom import Identified
from django.http import HttpResponse
from django.shortcuts import render,redirect

from courses.models import Course,Video,Payment
from E_learing.settings import *
from datetime import datetime
from time import time
from django.views.decorators.csrf import csrf_exempt

import razorpay
client = razorpay.Client(auth=(KEY_ID , KEY_SECRET))

def checkout(request,slug):
    course = Course.objects.get(slug = slug)


    if((request.user.is_authenticated is False)):
        return redirect('login')
    user = request.user
    action = request.GET.get('action')
    order  = None
    payment = None
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
        payment = Payment()
        payment.user = user
        payment.course = course
        payment.order_id = order.get('id')
        payment.save()
    context = {
        "course" : course,
        "order" :order,
        "payment":payment,
        'user':user
    }
    return render(request,template_name="courses/check_out.html",context=context)

@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        context ={
            
        }
        try:
          client.utility.verify_payment_signature(data)
          return render(request,template_name="courses/my_courses.html",context=context)
        except:
            return HttpResponse("dfsdfs invalid")
        print(request.POST)


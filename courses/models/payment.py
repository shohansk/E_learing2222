from django.db import models

from courses.models import Course

from courses.models import UserCourse
from django.contrib.auth.models import User

class Payment((models.Model)):
    user = user_course = models.ForeignKey(User,null= True ,on_delete= models.CASCADE)
    order_id = models.CharField(max_length=100,null=False)
    payment_id = models.CharField(max_length=100)
    user_course = models.ForeignKey(UserCourse,null= True,blank=True ,on_delete= models.CASCADE)
    course = models.ForeignKey(Course ,on_delete= models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add= True)
   
    
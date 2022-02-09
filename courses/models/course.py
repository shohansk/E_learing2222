from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length= 150 , null=False)
    slug = models.CharField(max_length= 100 , null=True)
    description = models.CharField(max_length=250 , null=True)
    price = models.IntegerField(null= False )
    discount = models.IntegerField(null=False,default=0)
    active = models.BooleanField(default= False)
    thumbnail = models.ImageField(upload_to = "files/thumbnail" )
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to= "files/resource")
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name
    
    

class CourseProperty((models.Model)):
    description =  models.CharField(max_length= 50 ,null= False)
    course = models.ForeignKey(Course,null= False ,on_delete= models.CASCADE)

    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass
    

class Prerequisite(CourseProperty):
    pass

class Learing(CourseProperty):
    pass


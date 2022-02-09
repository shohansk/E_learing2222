
from django.http import HttpResponse
from django.shortcuts import redirect, render
from courses.forms.login_form import LoginForm


from courses.models import Course,Video
from courses.forms import ResgistrationFrom
from django.views import View


class SignUp(View):
    def get(self,request):
        form = ResgistrationFrom()
        return render(request,template_name="courses/signup_page.html",context= {'form': form})

    def post(self,request):
        
        form = ResgistrationFrom(request.POST)
        if(form.is_valid()):
            user = form.save()
            if(user):
                return redirect('login')

        return render(request,template_name="courses/signup_page.html",context= {'form': form})


        
    



class Login(View):
    def get(Self ,request):
        form = LoginForm()
        context = {
            "form" : form
        }
        return render(request,template_name="courses/login_page.html",context= {'form': form})

    def post(self,request):
        return HttpResponse("DSfsdf")


    
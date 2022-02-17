
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from E_learing.settings import MEDIA_ROOT ,MEDIA_URL
from courses.models import course

from courses.views import home,CoursePage,checkout,verifyPayment
from courses.views.auth import SignUp,Login,signout
urlpatterns = [
    path('',home , name = 'home'),
     path('logout',signout , name = 'logout'),
    path('signup',SignUp.as_view(), name = 'signup'),
    path('login',Login.as_view() , name = 'login'),
    path('course/<str:slug>',CoursePage ,name = 'coursepage'),
    path('check-out/<str:slug>',checkout ,name = 'check_out'),
    path('verify_payment/<str:slug>',verifyPayment ,name = 'my_courses')



    
] 

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

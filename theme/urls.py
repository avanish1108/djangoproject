from django.urls import path
from .views import mailsend, success,index

app_name = 'theme'

urlpatterns = [
    path('sendmail/', mailsend, name="mailsend"),
    path('',index,name="index"),
    path('success/', success, name="success"),

]
from django.urls import path
from register import views
from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static 
app_name = 'register'

urlpatterns=[
    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login')

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
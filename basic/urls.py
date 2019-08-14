from django.urls import path
from . import views

app_name = 'basic'

urlpatterns = [
    path('', views.DetailList.as_view(template_name='basic/detail_list.html'), name='detail_list'),
    path('new',views.DetailCreate.as_view(template_name='basic/detail_form.html'), name='detail_create'),
    path('edit/<int:pk>',views.DetailUpdate.as_view(template_name='basic/detail_form.html'), name='detail_edit'),
    path('delete/<int:pk>',views.DetailDelete.as_view(template_name='basic/detail_confirm_delete.html'), name='detail_delete'),

]
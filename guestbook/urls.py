from django.urls import path
from . import views

app_name = 'guestbook'

urlpatterns = [
    path('', views.guest_list, name='index'),
    path('list', views.guest_list, name='list'),
    path('write', views.guest_write, name='write'),
    path('deleteform/<int:id>', views.deleteform, name='deleteform'),
]

from django.urls import path
from . import views

app_name = 'hobby'

urlpatterns = [
    path('', views.HobbyModelView.as_view(), name='index'),
    path('Idol/', views.IdolList.as_view(), name='idol_list'),
    path('Member/', views.MemberList.as_view(), name='member_list'),
    path('Ent/', views.EntList.as_view(), name='ent_list'),
    path('Idol/<int:pk>/', views.IdolDetail.as_view(), name='idol_detail'),
    path('Member/<int:pk>/', views.MemberDetail.as_view(), name='member_detail'),
    path('Ent/<int:pk>/', views.EntDetail.as_view(), name='ent_detail'),
]

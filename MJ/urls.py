from django.contrib import admin
from django.urls import include, path
from MJ import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('home2', views.HomeView2.as_view(), name='home2'),
    path('home_error/', views.HomeErrorView.as_view(), name='home_error'),
    path('common/', include('common.urls')),
    path('intro/', views.IntroView.as_view()),
    path('sns/', views.SNSView.as_view()),
    path('hobby/', include('hobby.urls')),
    path('guestbook/', include('guestbook.urls')),
]

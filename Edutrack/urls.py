
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index_redirect, name='index_redirect'),
    path('web/', include('web.urls')),
    path('attendence/', views.attendence, name='attendence'),
    path('about/', views.about, name='about'),
    path('examination/', views.examination, name='examination'),
    path('timeTable/', views.timeTable, name='timeTable'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('explore/', views.explore, name='explore'),
    path('', views.firstpage, name='firstpage'),
    path('pysoprofile/', views.pysoprofile, name='pysoprofile'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('contact/', views.contact, name='contact'),
    
]


from django.contrib import admin
from django.urls import path, include


#Website

urlpatterns = [

    path('admin/', admin.site.urls), 
    #path('index/', views.index, name="index"),
    path('', include('music.urls')),
    
]

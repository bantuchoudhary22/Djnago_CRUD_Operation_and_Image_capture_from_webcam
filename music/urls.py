from django.urls import path
from.import views
from music.views import user_login, user_logout,success # Session 

#music
urlpatterns=[
path('',views.dashboard, name='dashboard'),
path('signup/', views.signup, name='signup'),

path( 'all/', views.all, name='all'),

path('insert/', views.insert, name='insert'),

path('insert/music/all.html',views.all,name='all'),

path('album_insert',views.albumInsert,name='album_insert'),

path('song_insert', views.songInsert, name='song_insert'),


path('register', views.register, name='register'),

path('update_album/<str:pk>',views.updatealbum,name='update_album'),

path('deletealbum/<str:pk>', views.deletealbum,name='deletealbum'),

path('update_song/<str:pk>',views.updatesong,name='update_song'),
#Session 
path('login/',user_login, name='user_login'),
path('success/', success, name='user_success'),
path('logout/', user_logout, name='user_logout'),

]
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from music.models import Album,Song,Register
from .forms import AlbumForm
from .forms import SongForm,RegisterForm
from django.contrib.auth import authenticate, login, logout # session authentication
import os

# Create your views here.
#music
def dashboard(request):
    return render(request, 'music/dashboard.html')

def signup(request):
    return render(request, 'music/signup.html')

def all(request):
    album= Album.objects.all()
    songs=Song.objects.all()
    registers=Register.objects.all()
    p={'album':album,'songs':songs,'registers':registers }
    return render(request, 'music/all.html',p)    
def insert(request):
    artist=request.POST.get['artist']
    genre=request.POST['genre']
    album_name=request.POST['album_name']
    data=Album(artist=artist, genre=genre,album_name=album_name )
    data.save()    
    return render(request, 'music/insert.html')

def albumInsert(request):
    form=AlbumForm()
    if request.method=='POST':
        form=AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all/')
    context={'form':form}
    return render(request,'music/album.html',context)
def songInsert(request):
    songinfo=SongForm()
    if request.method=='POST':
        songinfo=SongForm(request.POST)
        if songinfo.is_valid():
            songinfo.save()
            return redirect('all/')
    data={'songinfo':songinfo}
    return render(request,'music/song.html', data)        

def register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('all/')
    reg={'form':form}        
    return render(request, 'music/register.html',reg)

def updatealbum(request,pk):
    albums=Album.objects.get(id=pk)
    form=AlbumForm(instance=albums)
    if request.method=='POST':
        form=AlbumForm(request.POST,instance=albums)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'music/album.html',context)

def deletealbum(request, pk):
    albums=Album.objects.get(id=pk)
    if request.method =='POST':
        albums.delete()
        return redirect('/')
    context={'form':albums}
    return render (request,'music/deletealbum.html', context)

def updatesong(request,pk):
    songs=Song.objects.get(id=pk)
    songinfo=SongForm(instance=songs)
    if request.method=='POST':
        songinfo=SongForm(request.POST, instance=songs)
        if songinfo.is_valid():
            songinfo.save()
            return redirect('/')

    context={'songinfo': songinfo}
    return render(request, 'music/song.html', context)
# Session 
def user_login(request):
	context ={}
	if request.method =="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect(reverse("user_success"))
		else:
			context["error"]="Provide valid credential"
			return render (request, "music/login.html", context)

	else:
		return render(request,"music/login.html", context)

def success(request):
	context={}
	context['user']= request.user
	return render(request, "music/success.html", context)

	

def user_logout(request):
	if request.method =="POST":
		logout(request)
		return HttpResponseRedirect(reverse('user_login'))

def gallery(request):

    path="C:\\somedirectory" # insert the path to your directory
    img_list =os.listdir(path)
    return render_to_response('gallery.html', {'images': img_list})

# Session 	    
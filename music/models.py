from django.db import models

# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=100)
    genre=models.CharField(max_length=50)
    album_name=models.CharField(max_length=100)


    def __str__(self):
          return  self.artist+' - ' + self.genre+' - '+self.album_name


class Song(models.Model):
    file_type=models.CharField(max_length=20)
    song_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.file_type+' - ' +self.song_name 

class Register(models.Model):
     first_name=models.CharField(max_length=50)
     last_name= models.CharField(max_length=50)
     email=models.EmailField()
     password= models.CharField(max_length=10)

     def  __str__(self):
        return  self.first_name+ '-'+self.last_name


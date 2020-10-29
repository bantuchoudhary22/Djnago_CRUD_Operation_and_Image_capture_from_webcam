from django.forms import ModelForm
from .models import Album,Song,Register


class AlbumForm(ModelForm):
    class Meta:
        model=Album
        
        fields='__all__'
class SongForm(ModelForm):
    class Meta:
        model=Song
        fields='__all__'
class RegisterForm(ModelForm):
    class Meta:
        model=Register 
        fields='__all__'       
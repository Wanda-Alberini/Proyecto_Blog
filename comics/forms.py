from django import forms
from ckeditor.widgets import CKEditorWidget  
from .models import Articulo

class ArticuloFormulario(forms.ModelForm):
    cuerpo = forms.CharField(widget=CKEditorWidget(config_name='default'))  

    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha_publicacion', 'imagen']
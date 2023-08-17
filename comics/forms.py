from django import forms
from .models import Articulo  # Asegúrate de importar tu modelo Articulo

class ArticuloFormulario(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha_publicacion', 'imagen']

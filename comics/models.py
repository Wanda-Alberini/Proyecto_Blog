from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=1500)
    autor = models.CharField(max_length=256)
    fecha_publicacion = models.DateField(null=True)
    imagen = models.ImageField(upload_to='articulos/')
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


  
    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.fecha_publicacion}"
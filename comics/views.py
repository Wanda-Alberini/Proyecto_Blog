from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from comics.models import  Articulo
from .forms import ArticuloFormulario


#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# #vistas basadas en clases

#Vistas de Articulos
class ArticuloListView(ListView):
    model = Articulo
    template_name = 'comics/lista_articulos.html' 

#Crear un Articulo
#Se requiere autentificar
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloFormulario  # Utiliza el formulario basado en un modelo
    success_url = reverse_lazy('listar_articulos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#Ver Detalle de un Articulo
#NO Se requiere autentificar
class ArticuloDetailView(DetailView):
    model = Articulo
    succes_url= reverse_lazy('listar_articulos') 

#Editar un Articulo
#Se requiere autentificar

class ArticuloUpdateView(LoginRequiredMixin,UpdateView):
    model = Articulo
    fields = ( 'titulo','subtitulo', 'cuerpo', 'autor', 'fecha_publicacion')
    success_url = reverse_lazy('listar_articulos')

   # Minuto 17 clase 24
    def form_valid(self, form):
        if self.request.user != self.object.user:
            form.add_error(None, "No tienes los permisos necesarios para realizar esta acción. Debes ser el usuario creador para poder editar.")
            return super().form_invalid(form)
        return super().form_valid(form) 
    
#Borrar un Articulo
#Se requiere autentificarse
class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('listar_articulos')   

    def form_valid(self, form):
        if self.request.user != self.object.user:
            form.add_error(None, "No tienes los permisos necesarios para realizar esta acción. Debes ser el usuario creador para poder eliminar.")
            return super().form_invalid(form)
        return super().form_valid(form) 
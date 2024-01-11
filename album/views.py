from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_album(request):
    album_form = forms.AlbumForm()
    return render(request, 'edit_album.html', {'form': album_form})

@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView):
    form_class = forms.AlbumForm
    template_name = 'edit_album.html'
    success_url = reverse_lazy('edit_album.html')

@login_required
def edit_album(request, id):
    album = models.Album.objects.get(pk = id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
        
    return render(request, 'edit_album.html', {'form': album_form})

@method_decorator(login_required, name='dispatch')
class EditAlbum(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'edit_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('edit_album.html')

@login_required
def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')

@method_decorator(login_required, name='dispatch')
class DeleteAlbum(DeleteView):
    model = models.Album
    template_name = 'delete_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
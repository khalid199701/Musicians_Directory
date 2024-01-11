from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms
# Create your views here.
@login_required
def edit_musician(request):
    musician_form = forms.MusicianForm
    return render(request, 'edit_musician.html', {'form': musician_form})

@method_decorator(login_required, name='dispatch')
class EditMusician(CreateView):
    form_class = forms.MusicianForm
    template_name = 'edit_musician.html'
    success_url = reverse_lazy('edit_musician.html')
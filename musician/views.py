from django.shortcuts import render
from . import forms
# Create your views here.
def edit_musician(request):
    musician_form = forms.MusicianForm
    return render(request, 'edit_musician.html', {'form': musician_form})
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from album.models import Album
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

def home(request):
    data = Album.objects.all()
    return render(request, 'home.html', {'data': data})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request= request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)
                if user is not None:
                    login(request, user)
                    return redirect('homepage')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('homepage')
    
class UserLogin(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('homepage')

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

def user_logout(request):
    logout(request)
    return redirect('user_login')

@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        return super().form_valid(form)
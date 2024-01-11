from django.urls import path, include
from . import views
urlpatterns = [
    # path('edit/', views.edit_musician, name = 'edit_musician'),
    path('edit/', views.EditMusician.as_view(), name = 'edit_musician'),
]
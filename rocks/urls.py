from django.urls import path
from . import views

urlpatterns = [
    path('', views.adoptions, name='adoptions'),
]

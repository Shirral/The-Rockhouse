from django.urls import path
from . import views

urlpatterns = [
    path('', views.adoptions, name='adoptions'),
    path('rockprofile/', views.rockprofile, name='rockprofile'),
]

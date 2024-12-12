from django.urls import path
from . import views

urlpatterns = [
    path('', views.adoptions, name='adoptions'),
    path('rockprofile/<int:rock_id>/', views.rockprofile, name='rockprofile'),
    path('rock/edit/<int:rock_id>/', views.rock_edit, name='rock_edit'),
]

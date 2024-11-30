from django.urls import path
from . import views

urlpatterns = [
    path('<int:rock_id>/', views.adoption_confirm, name='adoption_confirm'),
    path('form/<int:rock_id>/', views.adoption_form, name='adoption_form'),
    path('success/<adoption_number>/', views.adoption_success, name='adoption_success'),
]

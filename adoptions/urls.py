from django.urls import path
from . import views

urlpatterns = [
    path('<int:rock_id>/', views.adoption_confirm, name='adoption_confirm'),
]

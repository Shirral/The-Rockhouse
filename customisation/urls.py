from django.urls import path
from . import views

urlpatterns = [
    path('<int:rock_id>/', views.customisation, name='customisation'),
    path(
        'accessory_request/',
        views.accessory_request,
        name='accessory_request'
        ),
]

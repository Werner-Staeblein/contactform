from django.urls import path
from . import views
urlpatterns = [
     path('', views.contact_view, name='contact_form'),
     path('success/', views.form_success_view, name='form_success'),
]

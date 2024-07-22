from django.urls import path
from . import views
from .views import HomePage, LoguinPage


urlpatterns = [
    path('', views.HomePage, name='HomePage'),

    path('loguin/', views.LoguinPage, name='LoguinPage'),


] 



from django.urls import path

from . import views

app_name='theodinproject'
urlpatterns = [
    path('', views.index, name='index'),
]

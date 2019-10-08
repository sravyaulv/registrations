from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('insert/', views.insert, name='insert'),
    path('fetchData/', views.fetch_all_data, name='fetch_data')
]
from django.urls import path
from . import views


urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('', views.home, name='home'),
    path('create_group/', views.create_pickup_group, name='create_group'),
]
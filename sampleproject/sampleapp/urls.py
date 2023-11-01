from . import views
from django.urls import path

urlpatterns = [

    path('', views.sample, name='sample')
    # path('add/', views.addition, name='addition'),
    # path('add/', views.subtraction, name='subtraction')
    # path('robots/', views.robots, name='robots'),

]
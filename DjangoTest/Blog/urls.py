from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='StartPage'),
    path('Detail/<int:Number>', views.read, name='DetailPage')
]
from django.urls import path
from application import views 

urlpatterns = [
    path('result/', views.result, name='result'),
]
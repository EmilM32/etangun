from django.urls import path
from . import views

urlpatterns = [
    path('test_function/', views.test_function),
]
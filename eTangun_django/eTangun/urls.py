from django.urls import path
from . import views

urlpatterns = [
    path('get_belt_level/', views.get_belt_level),
    path('save_new_member/', views.save_new_member),
    path('get_all_members/', views.get_all_members)
]
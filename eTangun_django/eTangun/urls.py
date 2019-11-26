from django.urls import path
from . import views

urlpatterns = [
    path('get_belt_level/', views.get_belt_level),
    path('save_new_member/', views.save_new_member),
    path('get_all_members/', views.get_all_members),
    path('get_all_addresses/', views.get_all_addresses),
    path('add_new_address/', views.add_new_address),
    path('edit_address/', views.edit_address),
    path('delete_address/', views.delete_address),
    path('login_user/', views.login_user)
]

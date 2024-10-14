from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_jobfinder, name='create-jobfinder'),
    path('search/', views.retrieve_jobfinder, name='retrieve-jobfinder'),
    path('update/<int:pk>', views.update_jobfinder, name='update-jobfinder'),
    path('delete/<int:pk>', views.delete_jobfinder, name='delete-jobfinder'),
    path('entreprises/', views.create_entreprise, name='create-entreprise'),
    path('search-entreprise/', views.retrieve_entreprise, name='retrieve-entreprise'),
    path('update-entreprise/<int:pk>', views.update_entreprise, name='update_entreprise'),
    path('delete-entreprise/<int:pk>', views.delete_entreprise, name='delete-entreprise'),

]

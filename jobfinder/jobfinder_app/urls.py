from django.urls import path
from .views import *

# urlpatterns = [
#     path('', views.create_annonce, name='create-jobfinder'),
#     path('search/', views.retrieve_jobfinder, name='retrieve-jobfinder'),
#     path('update/<int:pk>', views.update_jobfinder, name='update-jobfinder'),
#     path('delete/<int:pk>', views.delete_jobfinder, name='delete-jobfinder'),
# ]

urlpatterns = [
    path('', home_page, name='home_page'),
    path('recherche_page/', recherche_page, name='recherche_page'),
    path('connexion_page/', connexion_page, name='connexion_page'),
    path('inscription_page/', inscription_page, name='inscription_page'),
    path('annonce_form/', annonce_entry, name='annonce_form'),
    path('process_annonce_entry/', process_annonce_entry, name='process_annonce_entry'),
    path('candidature_form/', candidature_entry, name='candidature_form'),
    
]
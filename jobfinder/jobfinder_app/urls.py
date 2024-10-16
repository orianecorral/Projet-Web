from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    # path('recherche_page/', recherche_page, name='recherche_page'),
    path('connexion_page/', connexion_page, name='connexion_page'),
    path('inscription_page/', inscription_page, name='inscription_page'),
    path('annonce_form/<int:pk>', annonce_entry, name='annonce_form'),
    # path('process_annonce_entry/', process_annonce_entry, name='process_annonce_entry'),
    path('candidature_form/', candidature_entry, name='candidature_form'),
    # Pour logout user
    path('logout_user/', logout_user, name='logout_user'),
    path('logout_entreprise/', logout_entreprise, name='logout_entreprise'),
    # delete compte
    
]

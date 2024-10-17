from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    # path('recherche_page/', recherche_page, name='recherche_page'),
    path('connexion_page/', connexion_page, name='connexion_page'),
    path('inscription_page/', inscription_page, name='inscription_page'),

    # Annonce form 
    path('annonce_form/<int:pk>', annonce_entry, name='annonce_form'),

    # Candidature form pour les personnes sans compte
    path('no_compte_candidature_form/<int:pk>', no_compte_candidature_entry, name='no_compte_candidature_form'),

    # Candidature form pour les personnes avec compte
    path('compte_candidature_form/<int:pk>/<int:pz>', compte_candidature_entry, name='compte_candidature_form'),

    # Pour logout user
    path('logout_user/', logout_user, name='logout_user'),
    path('logout_entreprise/', logout_entreprise, name='logout_entreprise'),
    # delete compte

]

from django.urls import path
from .views import *

app_name = "jobfinder_compte"

urlpatterns = [
    # Connexion-Log in
    path('connexion_entreprise/', connexion_entreprise, name='connexion_entreprise'),
    path('connexion_user/', connexion_user, name='connexion_user'),
    path('entreprise_form/', entreprise_form, name='entreprise_form'),

    path('user_form/', user_form, name='user_form'),
    path('entreprise_page/', entreprise_page, name='entreprise_page'),
    path('user_page/', user_page, name='user_page'),

    # Logout
    # path('logout_entreprise/', logout_entreprise, name='logout_entreprise'),
    # path('logout_user/', logout_user, name='logout_user'),



]

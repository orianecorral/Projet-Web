from django.urls import path, include
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
    path('update_user/<int:pk>', update_user_bis, name='update_user'),
    path('update_entreprise/<int:pk>', update_entreprise, name='update_entreprise'),
    path('update_annonce/<int:pk>', update_annonce, name='update_annonce'),
    path('delete_particulier/<int:pk>', delete_particulier, name='delete_particulier'),
    path('delete_entreprise/<int:pk>', delete_entreprise, name='delete_entreprise'),
    path('delete_annonce/<int:pk>', delete_annonce, name='delete_annonce')



]

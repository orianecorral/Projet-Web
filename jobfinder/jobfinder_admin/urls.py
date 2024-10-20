from django.urls import path
from .views import *
urlpatterns = [ 
    path('admin_table/', tab_Particulier, name='admin_table'),
    path('liste_candidature/<int:pk>', liste_candidature, name='liste_candidature'),

    path('ccc/', CoAdmin, name='ccc'), #a choisi un code improbable tout simplement pour renforcer la sécurité

    # URL des création de Articulier Entreprise et Annonces

    path('form_user/', form_user, name='form_user'),
    path('form_entreprise/', form_entreprise, name='form_entreprise'),
    path('form_annonce/<int:pk>', form_annonce, name='form_annonce'),
] 

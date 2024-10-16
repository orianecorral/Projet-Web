from django.urls import path
from .views import *
urlpatterns = [ 
    path('tab_Particulier/', tab_Particulier, name='tab_Particulier'),
    path('tab_entreprise/', tab_entreprise, name='tab_entreprise'),
    path('tab_annonce/', tab_annonce, name='tab_annonce'),
] 

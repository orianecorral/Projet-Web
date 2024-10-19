from django.urls import path
from .views import *
urlpatterns = [ 
    path('tab_Particulier/', tab_Particulier, name='tab_Particulier'),
    path('ccc/', CoAdmin, name='ccc'), #a choisi un code improbable tout simplement pour renforcer la sécurité
] 

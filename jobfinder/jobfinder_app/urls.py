from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_jobfinder, name='create-jobfinder'),
    path('search/', views.retrieve_jobfinder, name='retrieve-jobfinder'),
    path('update/<int:pk>', views.update_jobfinder, name='update-jobfinder'),
    path('delete/<int:pk>', views.delete_jobfinder, name='delete-jobfinder'),
]

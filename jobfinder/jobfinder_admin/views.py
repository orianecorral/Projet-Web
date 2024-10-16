from django.shortcuts import render
from django.apps import apps
from jobfinder_compte.models import Particuliers
# Create your views here.
def administration(request):
    print('test')
    Particulier =Particuliers.objects.all()
    return render(request,'Liste_utilisateur.html',{'groupe':Particulier})
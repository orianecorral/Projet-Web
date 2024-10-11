# Create your views here.
from django.shortcuts import render, redirect
from .forms import AnnoncesForm
from .models import Annonces

def create_jobfinder(request):
    if request.method == "POST":
        form = AnnoncesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('search/')
            except:
                pass
    else:
        form = AnnoncesForm()
    return render(request, 'create.html', {'form':form})

def retrieve_jobfinder(request):
    annonces = Annonces.objects.all()
    return render(request,'search.html',{'Annonces':annonces} )

def update_jobfinder(request,pk):
    annonces = Annonces.objects.get(id=pk)
    form = AnnoncesForm(instance=annonces)

    if request.method == 'POST':
        form = AnnoncesForm(request.POST, instance=annonces)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'annonces': annonces,
        'form': form,
    }
    return render(request,'update.html',context)


def delete_jobfinder(request, pk):
    annonces = Annonces.objects.get(id=pk)

    if request.method == 'POST':
        annonces.delete()
        return redirect('/search')

    context = {
        'annonces': annonces,
    }
    return render(request, 'remove.html', context)

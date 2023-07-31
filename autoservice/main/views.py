from django.shortcuts import render, redirect
from .models import Rulevoe, Tormoz,Podveska, Dvigatel, Electron, Vihlop
from .forms import AddClient
#from models import Client


def index(request):
    return render(request,'main/index.html')


def service(request):
    rulevoe = Rulevoe.objects.all()
    tormoz = Tormoz.objects.all()
    podveska = Podveska.objects.all()
    dvigatel = Dvigatel.objects.all()
    electron = Electron.objects.all()
    vihlop = Vihlop.objects.all()
    return render(request,'main/service.html',
        {'rulevoe': rulevoe, 'tormoz': tormoz , 'podveska': podveska, 'dvigatel': dvigatel,'electron': electron,'vihlop': vihlop,})


def contact(request):
    return render(request,'main/contact.html')


def registr(request):
    #return render(request,'main/registr.html')
    if request.method == 'POST':
        form = AddClient(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except:
                form.add_error(None, 'Ошибка заполнения')
    else:
        form = AddClient()
    return render(request, 'main/registr.html', {'form': form})
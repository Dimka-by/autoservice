from rest_framework import viewsets
from . import models
from . import serializers


class RulevoeViewset(viewsets.ModelViewSet):
    queryset = models.Rulevoe.objects.all()
    serializer_class = serializers.RulevoeSerializer


class TormozViewset(viewsets.ModelViewSet):
    queryset = models.Tormoz.objects.all()
    serializer_class = serializers.TormozSerializer


class PodveskaViewset(viewsets.ModelViewSet):
    queryset = models.Podveska.objects.all()
    serializer_class = serializers.PodveskaSerializer


class DvigatelViewset(viewsets.ModelViewSet):
    queryset = models.Dvigatel.objects.all()
    serializer_class = serializers.DvigatelSerializer


class ElectronViewset(viewsets.ModelViewSet):
    queryset = models.Electron.objects.all()
    serializer_class = serializers.ElectronSerializer


class VihlopViewset(viewsets.ModelViewSet):
    queryset = models.Vihlop.objects.all()
    serializer_class = serializers.VihlopSerializer


class ClientViewset(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
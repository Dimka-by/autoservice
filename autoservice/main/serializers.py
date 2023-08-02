from rest_framework import serializers
from . import models


class RulevoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rulevoe
        fields =('id', 'work_type', 'price')


class TormozSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tormoz
        fields =('id', 'work_type', 'price')


class PodveskaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Podveska
        fields =('id', 'work_type', 'price')



class DvigatelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dvigatel
        fields =('id', 'work_type', 'price')



class ElectronSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Electron
        fields =('id', 'work_type', 'price')


class VihlopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vihlop
        fields =('id', 'work_type', 'price')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields =('id', 'name', 'email', 'phone', 'car')

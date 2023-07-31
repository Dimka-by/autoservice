from django.db import models


class Rulevoe(models.Model):
    id = models.IntegerField(primary_key=True)
    work_type = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)


    def __str__(self):# отображение в админ панеле название строки
        return self.work_type


class Tormoz(models.Model):
    id = models.IntegerField(primary_key=True)
    work_type = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)

    def __str__(self):  # отображение в админ панеле название строки
        return self.work_type


class Podveska(models.Model):
    id = models.IntegerField(primary_key=True)
    work_type = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)

    def __str__(self):# отображение в админ панеле название строки
        return self.work_type


class Dvigatel(models.Model):
    id = models.IntegerField(primary_key=True)
    work_type = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)

    def __str__(self):# отображение в админ панеле название строки
        return self.work_type


class Electron(models.Model):
    id = models.IntegerField(primary_key=True)
    work_type = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)

    def __str__(self):# отображение в админ панеле название строки
        return self.work_type


class Vihlop(models.Model):
    id = models.IntegerField(primary_key=True)
    work_type = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)

    def __str__(self):# отображение в админ панеле название строки
        return self.work_type


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    car = models.CharField(max_length=200)

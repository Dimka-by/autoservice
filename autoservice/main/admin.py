from django.contrib import admin
from .models import *

# регистрация моделей в админ панеле
admin.site.register(Rulevoe)
admin.site.register(Tormoz)
admin.site.register(Podveska)
admin.site.register(Dvigatel)
admin.site.register(Electron)
admin.site.register(Vihlop)
admin.site.register(Client)
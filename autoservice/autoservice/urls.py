from django.contrib import admin
from django.urls import path
from django.urls import include
from .api import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/', include(router.urls)),
]

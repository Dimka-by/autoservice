from rest_framework import routers
from main import api_views as main_views


router = routers.DefaultRouter()
router.register(r'rulevoe', main_views.RulevoeViewset)
router.register(r'tormoz', main_views.TormozViewset)
router.register(r'podveska', main_views.PodveskaViewset)
router.register(r'dvigatel', main_views.DvigatelViewset)
router.register(r'electron', main_views.ElectronViewset)
router.register(r'vihlop', main_views.VihlopViewset)
router.register(r'client', main_views.ClientViewset)
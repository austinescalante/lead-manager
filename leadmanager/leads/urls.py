#Use router from rest framework
#REST framework adds support for automatic URL routing to Django, and provides you with a simple, 
#quick and consistent way of wiring your view logic to a set of URLs
from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads',LeadViewSet,'leads')

urlpatterns=router.urls
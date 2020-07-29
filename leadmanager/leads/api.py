#Creation of api

from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

#Lead ViewSet: Allows us to create a CRUD api without specifiying specific methods
#A ViewSet class is simply a type of class-based View, that does not provide any method handlers 
#such as .get() or .post(), and instead provides actions such as .list() and .create().

class LeadViewSet(viewsets.ModelViewSet):
    queryset=Lead.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=LeadSerializer
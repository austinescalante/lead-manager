from rest_framework import serializers
from .models import Lead
#Serializers allow complex data such as querysets and model instances to be converted to 
#native Python datatypes that can then be easily rendered into JSON, XML or other content types.
#Lead Serializer

#Creating a user with a nested profile object.
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields='__all__'
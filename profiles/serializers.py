from rest_framework import serializers

from .models import Profiles

class ProfileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Profiles
        fields = "__all__"
from rest_framework import serializers
import re
from rest_framework.exceptions import ValidationError

from .models import Profiles

class ProfileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Profiles
        fields = "__all__"

    def validate_phone_number(self , value):
        phone_number_pattern = re.compile("09\d{9}$")
        if phone_number_pattern.match(value):
            return value
        raise ValidationError("{phone_number is not correct}")
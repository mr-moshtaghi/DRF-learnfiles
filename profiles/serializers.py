from rest_framework import serializers
import re
from rest_framework.exceptions import ValidationError

from .models import Profiles
from posts.serializers import PostsSerializers

class ProfileSerializers(serializers.ModelSerializer):

    posts = PostsSerializers( many = True , read_only=True)
    
    class Meta:
        model = Profiles
        fields = "__all__"

    def validate_phone_number(self , value):
        phone_number_pattern = re.compile("09\d{9}$")
        if phone_number_pattern.match(value):
            return value
        raise ValidationError("{phone_number is not correct}")
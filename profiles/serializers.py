from rest_framework import serializers
import re
from rest_framework.exceptions import ValidationError

from .models import Profiles
from posts.models import Posts
from posts.serializers import PostsSerializers

class ProfileSerializers(serializers.ModelSerializer):

    posts = PostsSerializers( many = True , read_only=True)
    post = PostsSerializers(write_only=True)
    
    class Meta:
        model = Profiles
        fields = "__all__"

    def validate_phone_number(self , value):
        phone_number_pattern = re.compile("09\d{9}$")
        if phone_number_pattern.match(value):
            return value
        raise ValidationError("{phone_number is not correct}")

    def create(self , validate_data):
        post = validate_data.pop("post")
        my_author = Profiles.objects.create(**validate_data)
        my_post = Posts.objects.create(**post , author=my_author)
        return my_author

from rest_framework import serializers

from .models import Posts

class PostsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Posts
        fields = '__all__'
        extra_kwargs = {'author':{'required':False}}
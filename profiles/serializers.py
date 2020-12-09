from rest_framework import serializers

class ProfileSerializers(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    first_name = serializers.CharField(max_length=50)
    last_anme = serializers.CharField(max_length=70)
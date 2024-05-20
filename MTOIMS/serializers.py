# serializers.py
from djoser.serializers import UserSerializer

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'username',)  # Include 'id' field in the serializer

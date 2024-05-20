# views.py
from djoser.views import UserViewSet
from .serializers import CustomUserSerializer

class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserSerializer

    def get_serializer_class(self):
        if self.action == 'me':
            return CustomUserSerializer
        return super().get_serializer_class()

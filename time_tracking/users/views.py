from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from .serializers import UserSerializer, UserLoginSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_serializer_context(self):
        data = super().get_serializer_context()
        return data


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'status_code': status.HTTP_200_OK,
            'message': 'User logged in successfully',
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)
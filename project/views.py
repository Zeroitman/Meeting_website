from rest_framework.exceptions import ParseError
from trainees.settings import DATA_UPLOAD_MAX_NUMBER_FIELDS, API_SECURE_KEY
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import *


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if request.headers.get('API-SECURE-KEY') != API_SECURE_KEY:
            return Response({"result": "Invalid secure key"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            avatar = request.FILES['avatar']
            if avatar.size > DATA_UPLOAD_MAX_NUMBER_FIELDS:
                return Response({"result": "Avatar not valid"}, status=status.HTTP_400_BAD_REQUEST)
            new_request_data = request.data.copy()
            serializer = UserRegisterSerializer(data=new_request_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"result": "User created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            raise ParseError(ex)

from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from project.watemark import watermark_avatar
from trainees.settings import DATA_UPLOAD_MAX_NUMBER_FIELDS, API_SECURE_KEY
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from project.serializers import *


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


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
            del new_request_data['avatar']
            image = watermark_avatar(avatar.file)
            new_avatar = InMemoryUploadedFile(file=image, name=avatar.name, field_name=avatar.field_name,
                                              content_type=avatar.content_type, size=image.getbuffer().nbytes,
                                              charset=avatar.charset)
            new_request_data['avatar'] = new_avatar
            serializer = UserRegisterSerializer(data=new_request_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"result": "User created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            raise ParseError(ex)


@api_view(['GET'])
def user_list(request):
    if request.headers.get('API-SECURE-KEY') != API_SECURE_KEY:
        return Response({"result": "Invalid secure key"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        element = dict()
        name, surname, gender = request.data.get('name'), request.data.get('surname'), request.data.get('gender')
        if name:
            element['name'] = name
        if surname:
            element['surname'] = surname
        if gender:
            element['gender'] = gender
        users = User.objects.filter(**element)
        serializer = UserListSerializer(users, many=True)
        if serializer.data:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response({"result": "NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        raise ParseError(ex)

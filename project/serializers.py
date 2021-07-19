from project.models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'gender', 'password', 'password2', 'avatar', 'latitude', 'longitude']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
            surname=self.validated_data['surname'],
            gender=self.validated_data['gender'],
            avatar=self.validated_data['avatar'],
            latitude=self.validated_data['latitude'],
            longitude=self.validated_data['longitude'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        return token


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'is_active', 'is_staff', 'groups', 'user_permissions', 'is_superuser')


class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ()

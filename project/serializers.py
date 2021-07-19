from project.models import *
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'gender', 'password', 'password2', 'avatar']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
            surname=self.validated_data['surname'],
            gender=self.validated_data['gender'],
            avatar=self.validated_data['avatar']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user

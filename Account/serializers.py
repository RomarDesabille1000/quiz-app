from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'type', 'password']

    def create(self, validated_data):
        """ Creates and returns a new user """

        # Validating Data
        user = User(
            name=validated_data['name'],
            email=validated_data['email'],
            type=validated_data['type'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'type', 'password']

    def create(self, validated_data):
        """ Creates and returns a new user """
        print(validated_data)
        # Validating Data
        user = User(
            name=validated_data['name'],
            email=validated_data['email'],
            type=2,
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

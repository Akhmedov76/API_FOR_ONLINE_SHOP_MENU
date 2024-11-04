from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(min_length=50, write_only=True)
    phone_number = serializers.CharField(max_length=15, validators=[
        UniqueValidator(queryset=UserModel.objects.all(), message='Phone number already exists')])

    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'password', 'confirm_password']

        def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError('Passwords do not match')
            return data

        def create(self, validated_data):
            validated_data.pop('confirm_password')
            user = UserModel.objects.create_user(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user

        def validate_phone_number(self, phone_number: str):
            phone_number = phone_number.strip()
            if not phone_number.startswith('+998'):
                raise serializers.ValidationError('Phone number should start with +998')
            if not phone_number[4:].isdigit():
                raise serializers.ValidationError('Phone number should contain only digits')
            return phone_number


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(min_length=50, write_only=True)

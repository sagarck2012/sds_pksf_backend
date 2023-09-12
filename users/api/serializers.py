#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:14:00 2019

@author: sambhav
"""
from rest_framework import serializers
from users.models import User, Role
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.core.exceptions import ObjectDoesNotExist


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='id')
    email = serializers.EmailField(max_length=255, min_length=4),
    name = serializers.CharField(max_length=255, min_length=2)
    role_id = serializers.IntegerField(source='role.id')
    role_name = serializers.CharField(source='role.name')
    production_house = serializers.CharField()

    class Meta:
        model = User
        fields = ('user_id', 'name', 'email', 'phone_number', 'address', 'nid', 'role_id', 'role_name', 'production_house')
        # fields = ('name', 'email')


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'role','production_house', 'name', 'nid', 'phone_number', 'address')
        # fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}, 'nid': {'required': False}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        print(user)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']






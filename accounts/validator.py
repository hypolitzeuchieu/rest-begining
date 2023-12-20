from rest_framework import serializers
from .models import UserAccount


def validate_username(value):
    queryset = UserAccount.objects.filter(username__iexact=value)
    if queryset.exists():
        raise serializers.ValidationError(f"this {value} is already exist")
    return value


def validate_email(value):
    queryset = UserAccount.objects.filter(email__iexact=value)
    if queryset.exists():
        raise serializers.ValidationError(f"this {value} is already exist")
    return value

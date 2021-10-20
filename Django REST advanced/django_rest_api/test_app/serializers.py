from django.db import models
from rest_framework import serializers

from .models import Product

class SimpleSerializer(serializers.Serializer):

    product_tag = serializers.CharField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    stock = serializers.IntegerField()
    status = serializers.BooleanField(default=True)
    date_created = serializers.DateField(read_only=True)
    profile_picture = serializers.ImageField()

    class Meta:
        model = Product

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def upadte(self, validated_data):
        return Product.objects.all()

class StaticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
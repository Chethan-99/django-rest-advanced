from django.db.models import manager
from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import SimpleSerializer, StaticSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class SimpleAPIView(generics.GenericAPIView):
    serializer_class = SimpleSerializer
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data":serializer.data
        })

    def get(self, request):
        content = Product.objects.all()
        return Response({
            "data":SimpleSerializer(content, many=True).data
        })

class StaticView(ModelViewSet):
    serializer_class = StaticSerializer
    queryset = Product.objects.all()
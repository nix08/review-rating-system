from django.shortcuts import render
from rest_framework import generics,permissions
from.serializers import Reviewserializer
from .models import Review

# Create your views here.

class ReviewView(generics.CreateAPIView):
    serializer_class=Reviewserializer
    permission_classes=[permissions.AllowAny]
    
class ReviewListView(generics.ListAPIView):
    queryset=Review.objects.all()
    serializer_class=Reviewserializer
    permission_classes=[permissions.AllowAny]
    

from django.shortcuts import render
from rest_framework import generics,permissions
from django.db.models import Avg,Count
from rest_framework.views import APIView
from rest_framework.response import Response
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

class Reviewcounts(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self,request):
        reviews=Review.objects.all()
        Total_reviews=reviews.count() #total review count

        #avg rating
        Avg_rating=reviews.aggregate(Avg("rating"))["rating__avg"] or 0

        #distribution stars

        rating_counts=reviews.exclude(rating__isnull=True).values("rating").annotate(count=Count("rating"))
        Distribution={i:0 for i in range(1,6)}
        for rc in rating_counts:
            Distribution[rc["rating"]]=rc["count"]

        return Response({
            "Total_reviews":Total_reviews,
            "Avg_rating":Avg_rating,
            "Distribution_stars":Distribution

        }
        )

    

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movies.models import wishlist, watchedlist
from movies.serializers import WishlistSerializer, WatchedlistSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
import requests
from django.conf import settings
from django.db import IntegrityError
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ---------------------------------------------------------------------------------wishlist-----------------------------------------------------
class WishlistView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        items = wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "Already in your list."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, tmdb_id):
        try:
            wishlist_item = wishlist.objects.get(user=request.user, tmdb_id=tmdb_id)
            wishlist_item.delete()
            return Response({"message": "Wishlist item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except wishlist.DoesNotExist:
            return Response({"error": "Wishlist item not found."}, status=status.HTTP_404_NOT_FOUND)
    




# ------------------------------------------------------------------------------watchedlist-------------------------------------------------------------------
    
class WatchedlistView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        items = watchedlist.objects.filter(user=request.user)
        serializer = WatchedlistSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchedlistSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "Already in your list."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, tmdb_id):
        try:
            watchedlist_item = watchedlist.objects.get(user=request.user, tmdb_id=tmdb_id)
            watchedlist_item.delete()
            return Response({"message": "Watched list item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except watchedlist.DoesNotExist:
            return Response({"error": "Watched list item not found."}, status=status.HTTP_404_NOT_FOUND)

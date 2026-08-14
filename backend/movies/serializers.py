from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import wishlist, watchedlist
User = get_user_model()


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = wishlist
        fields = ['id', 'user', 'tmdb_id', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True},
            'created_at': {'read_only': True},
        }


class WatchedlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = watchedlist
        fields = ['id', 'user', 'tmdb_id', 'created_at', 'rating']
        extra_kwargs = {
            'user': {'read_only': True},
            'created_at': {'read_only': True},
        }
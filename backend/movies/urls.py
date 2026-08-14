from django.contrib import admin
from django.urls import path, include
from movies import views

urlpatterns = [
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('watchedlist/', views.WatchedlistView.as_view(), name='watchedlist'),
    path('wishlist/<int:tmdb_id>/', views.WishlistView.as_view(), name='wishlist-delete'),
    path('watchedlist/<int:tmdb_id>/', views.WatchedlistView.as_view(), name='watchedlist-delete'),

]
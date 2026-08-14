from django.contrib import admin
from django.urls import path, include
from accounts.views_token import RateLimitedTokenObtainPairView, RateLimitedTokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/movies/', include('movies.urls')),
    path('api/token/', RateLimitedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', RateLimitedTokenRefreshView.as_view(), name='token_refresh'),
]
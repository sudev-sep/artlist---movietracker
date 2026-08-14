from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


@method_decorator(ratelimit(key='ip', rate='10/m', method='POST', block=True), name='post')
class RateLimitedTokenObtainPairView(TokenObtainPairView):
    pass


@method_decorator(ratelimit(key='ip', rate='10/m', method='POST', block=True), name='post')
class RateLimitedTokenRefreshView(TokenRefreshView):
    pass
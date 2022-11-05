from django.urls import include, path
from rest_framework import routers
import rest_framework_simplejwt.serializers as jwt

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('follow', FollowViewSet, basename='follow')

jwt_patterns = [
    path(
        'create/', jwt.TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path('refresh/', jwt.TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', jwt.TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    path('v1/jwt/', include(jwt_patterns)),
    path('v1/', include(v1_router.urls)),
]

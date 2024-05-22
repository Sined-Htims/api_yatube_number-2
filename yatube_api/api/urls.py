from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CommentsViewSet, FollowViewSet, GroupsViewSet, PostsViewSet)

router = DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'groups', GroupsViewSet)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentsViewSet, basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

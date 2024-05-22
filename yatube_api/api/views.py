from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import filters, pagination, permissions, viewsets

from api.permissions import IsAuthor
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer)
from posts.models import Comment, Follow, Group, Post


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def get_permissions(self):
        actions = ('retrieve', 'create', 'list')
        for action in actions:
            if self.action == action:
                return super().get_permissions()
        return (IsAuthor(),)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupsViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get']


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        actions = ('retrieve', 'create', 'list')
        for action in actions:
            if self.action == action:
                return super().get_permissions()
        return (IsAuthor(),)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return Comment.objects.filter(post=self.get_post())

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    http_method_names = ['get', 'post']
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)  # почему и как? 'folowing'

    def retrieve(self, request, *args, **kwargs):
        raise Http404

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from shared.custom_pagination import CustomPagination
from .models import Post, PostLike, PostComment, CommentLike
from .serializers import PostSerializer, PostLikeSerializer, CommentLikeSerializer, CommentSerializer


class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Post.objects.all()
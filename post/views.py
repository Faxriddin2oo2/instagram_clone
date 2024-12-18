from django.core.serializers import serialize
from django.template.defaulttags import comment
from docs.conf import author
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shared.custom_pagination import CustomPagination
from .models import Post, PostLike, PostComment, CommentLike
from .serializers import PostSerializer, PostLikeSerializer, CommentLikeSerializer, CommentSerializer


class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Post.objects.all()


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def put(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True,
                "code": status.HTTP_200_OK,
                "message": "Post successfully updated",
                "data": serializer.data
            }
        )

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.delete()
        return Response(
            {
                "success": True,
                "code": status.HTTP_204_NO_CONTENT,
                "message": "Post successfully deleted",
            }
        )


class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = PostComment.objects.filter(post__id=post_id)
        return queryset


class PostCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        serializer.save(author=self.request.user, post_id=post_id)


class CommentListCreateApiView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = PostComment.objects.all()
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentRetrieveView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]
    queryset = PostComment.objects.all()


class PostLikeListView(generics.ListAPIView):
    serializer_class = PostLikeSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        return PostLike.objects.filter(post_id=post_id)

# class PostLikeCreateView(generics.CreateAPIView):
#     serializer_class = PostLikeSerializer
#     permission_classes = [IsAuthenticated, ]
#
#     def perform_create(self, serializer):
#         post_id = self.kwargs['pk']
#         serializer.save(author=self.request.user, post_id=post_id)
#
#
# class PostLikeDeleteView(generics.DestroyAPIView):
#     queryset = PostLike.objects.all()
#     serializer_class = PostLikeSerializer
#     permission_classes = [IsAuthenticated, ]
#
#     def delete(self, request, *args, **kwargs):
#         like = self.get_object()
#         like.delete()
#         return Response(
#             {
#                 "success": True,
#                 "code": status.HTTP_204_NO_CONTENT,
#                 "message": "Like successfully deleted",
#             }
#         )


class CommentLikeListView(generics.ListAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        comment_id = self.kwargs['pk']
        return CommentLike.objects.filter(comment_id=comment_id)


class PostLikeApiView(APIView):

    def post(self, request, pk):
        # try:
        #     post_like = PostLike.objects.get(
        #         author=self.request.user,
        #         post_id=pk
        #     )
        #     serializer = PostLikeSerializer(post_like)
        #     data = {
        #         "success" : True,
        #         "message" : "Postga LIKE muvaffaqiyatli qo'shildi",
        #         "data" : serializer.data
        #     }
        #     return Response(data, status=status.HTTP_201_CREATED)
        # except Exception as e:
        #     data = {
        #         "success": False,
        #         "message": f"{str(e)}",
        #         "data": None
        #     }
        #     return Response(data, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     try:
    #         post_like = PostLike.objects.get(
    #             author=self.request.user,
    #             post_id=pk
    #         )
    #         post_like.delete()
    #         data = {
    #             "success": True,
    #             "message": "LIKE muvaffaqiyatli o'chirildi",
    #             "data": None
    #         }
    #         return Response(data, status=status.HTTP_204_NO_CONTENT)
    #
    #     except Exception as e:
    #         data = {
    #             "success": False,
    #             "message": f"{str(e)}",
    #             "data": None
    #         }
    #         return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        try:
            post_like = PostLike.objects.get(
                author=self.request.user,
                post_id=pk
            )
            post_like.delete()
            data = {
                "success" : True,
                "message" : "LIKE muvaffaqiyatli o'chirildi"
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except PostLike.DoesNotExist:
            post_like = PostLike.objects.create(
                author=self.request.user,
                post_id=pk
            )
            serializer = PostLikeSerializer(post_like)
            data = {
                "success" : True,
                "message" : "Postga LIKE muvaffaqiyatli qo'shildi",
                "data" : serializer.data
            }
            return Response(data, status.HTTP_201_CREATED)


class CommentLikeApiView(APIView):
    def post(self, request, pk):
        try:
            comment_like = CommentLike.objects.get(
                author=self.request.user,
                comment_id=pk
            )
            comment_like.delete()
            data = {
                "success": True,
                "message": "LIKE muvaffaqiyatli o'chirildi",
                "data" : None
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except CommentLike.DoesNotExist:
            comment_like = PostComment.objects.create(
                author=self.request.user,
                post_id=pk
            )
            serializer = CommentLikeSerializer(comment_like)
            data = {
                "success": True,
                "message": "Izohga LIKE muvaffaqiyatli qo'shildi",
                "data": serializer.data
            }
            return Response(data, status.HTTP_201_CREATED)
    # def post(self, request, pk):
    #     try:
    #         comment_like = CommentLike.objects.create(
    #             author=self.request.user,
    #             comment_id=pk
    #         )
    #         serializer = CommentLikeSerializer(comment_like)
    #         data = {
    #             "success": True,
    #             "message": "Izohga LIKE muvaffaqiyatli qo'shildi",
    #             "data": serializer.data
    #         }
    #         return Response(data, status=status.HTTP_201_CREATED)
    #     except Exception as e:
    #         data = {
    #             "success": False,
    #             "message": f"{str(e)}",
    #             "data": None
    #         }
    #         return Response(data, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     try:
    #         comment_like = CommentLike.objects.get(
    #             author=self.request.user,
    #             comment_id=pk
    #         )
    #         comment_like.delete()
    #         data = {
    #             "success": True,
    #             "message": "LIKE muvaffaqiyatli o'chirildi",
    #             "data": None
    #         }
    #         return Response(data, status=status.HTTP_204_NO_CONTENT)
    #
    #     except Exception as e:
    #         data = {
    #             "success": False,
    #             "message": f"{str(e)}",
    #             "data": None
    #         }
    #         return Response(data, status=status.HTTP_400_BAD_REQUEST)




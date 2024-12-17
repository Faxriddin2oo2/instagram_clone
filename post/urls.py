from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, PostCommentListView, \
    PostCommentCreateView

urlpatterns = [
    path('posts/', PostListApiView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
    path('posts/<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('posts/<uuid:pk>/comments/', PostCommentListView.as_view()),
    path('posts/<uuid:pk>/comments/create/', PostCommentCreateView.as_view()),

    # path('posts/comments-create/', CommentCreateView.as_view()),
]
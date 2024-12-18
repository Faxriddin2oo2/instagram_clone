from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, PostCommentListView, \
    PostCommentCreateView, CommentListCreateApiView, PostLikeListView, CommentRetrieveView, \
    CommentLikeListView, PostLikeCreateView, PostLikeDeleteView

urlpatterns = [
    path('list/', PostListApiView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('<uuid:pk>/likes/', PostLikeListView.as_view()),
    path('<uuid:pk>/likes/create/', PostLikeCreateView.as_view()),
    path('<uuid:pk>/likes/delete/', PostLikeDeleteView.as_view()),
    path('<uuid:pk>/comments/', PostCommentListView.as_view()),
    path('<uuid:pk>/comments/create/', PostCommentCreateView.as_view()),

    path('comments/', CommentListCreateApiView.as_view()),
    path('comments/<uuid:pk>/', CommentRetrieveView.as_view()),
    path('comments/<uuid:pk>/likes/', CommentLikeListView.as_view()),


    # Vazifa
    # path('likes/')
    # path('likes/create/') +
    # path(likes/delete/') +
]
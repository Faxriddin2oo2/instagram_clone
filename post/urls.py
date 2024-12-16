from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView

urlpatterns = [
    path('posts/', PostListApiView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
    path('posts/<uuid:pk>', PostRetrieveUpdateDestroyView.as_view()),
]
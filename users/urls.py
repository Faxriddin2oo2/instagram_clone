from django.urls import path
from .views import CreateUserView, VerifyAPIView, GetNewVerification

urlpatterns = [
    path('signup/', CreateUserView.as_view()),
    path('verify/', VerifyAPIView.as_view()),
    path('new-verify/', GetNewVerification.as_view()),
]
from django.urls import path
from user.view.admin_login import AdminLoginView
from user.view.logout import LogoutView
from user.view.sign_up import SignUpView
from user.view.user import UserMeView

urlpatterns = [
    path('sign_up/', SignUpView.as_view()),
    path('login/', AdminLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('user_me/', UserMeView.as_view())
]
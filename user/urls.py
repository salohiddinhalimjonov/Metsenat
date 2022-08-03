from django.urls import path
from user.view.admin_login import AdminLoginView


urlpatterns = [
    path('login/', AdminLoginView.as_view())
]
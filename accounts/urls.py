from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name="registration/login.html",next_page='/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

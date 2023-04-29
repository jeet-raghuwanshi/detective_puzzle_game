from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('game/', views.game_view, name='game_view'),
        # ... your other URL patterns ...
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.register, name='register'),
]
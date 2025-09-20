from django.urls import path
from .import views

urlpatterns = [
    path('update/', views.update, name='update'),
    path('', views.registration, name="register"),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('forgot/', views.forgot_password, name='forgot'),
    path('password_changed', views.password_change, name='password_changed'),
]
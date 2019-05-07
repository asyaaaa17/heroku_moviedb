from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls

from . import views

app_name = 'user'
urlpatterns = [
    path('', include(urls)),
    path('register',
         views.RegisterView.as_view(),
         name='register'),
    path('login/',
         auth_views.LoginView.as_view(),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
]
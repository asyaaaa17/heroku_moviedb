from django.contrib import admin
from django.urls import path, include

from .views import email_view, success_view

urlpatterns = [
    path('email/', email_view, name='email'),
    path('success/', success_view, name='success')
]
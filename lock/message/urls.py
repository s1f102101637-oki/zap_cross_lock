from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.message_page, name='message'),
    path('profile/<str:name>/', views.profile_view, name='profile_view'),
    path('profile/<str:name>/', views.profile_view, name='profile_view'),
]

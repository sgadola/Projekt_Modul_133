from django.urls import path, include

from . import views


# app_name = "scriky"
urlpatterns = [
    path('register/', views.register_user, name='register'),

    # Administrative sites like login, logout, adminpage, etc
    path('', include('django.contrib.auth.urls')),
]

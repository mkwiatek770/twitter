from django.urls import path
from app import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("users/<str:username>/",
         views.UserDetailView.as_view(), name="user_detail"),

]

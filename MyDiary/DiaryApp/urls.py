from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name=""),
    path("sign-up", views.sign_up, name="sign-up"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashborad, name="dashboard"),
    path("logout", views.logout, name="logout"),

    path("create-diary", views.create_diary, name="create-diary"),

    path("view-diary", views.view_diary, name="view-diary"),

    path("update-diary/<str:pk>", views.update_diary, name="update-diary"),

    path("delete-diary/<str:pk>", views.delete_diary, name="delete-diary"),
]

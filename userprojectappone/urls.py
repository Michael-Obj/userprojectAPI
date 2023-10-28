from django.urls import path
from .import views


urlpatterns = [
    path("user/register", views.RegisterUser),
    path("user/login", views.LoginUser),
    # path("user/logout", views.LogoutUser),

    path("admin/register", views.RegisterSuperUser),
    path("admin/login", views.LoginSuperUser),
    
    # path("user/get/<str:username>/", views.GetUser),
    path("user/getall/", views.GetAllUsers),
    path("user/getid/<str:id>/", views.GetById),
    path("user/update/<str:id>/", views.UpdateUser),
    path("user/delete/<str:id>/", views.DeleteUser),
]


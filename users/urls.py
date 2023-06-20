from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('wishlist/', views.wishlist, name="wishlist"),
    #path('add_wishlist/<int:id>', views.add_wishlist, name="add_wishlist"),

]

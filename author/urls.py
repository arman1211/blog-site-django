from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('profile/', views.userprofile, name='profile'),
    path('edit-profile/', views.profie_update, name='editprofile'),
    path('profile/changepass', views.change_pass, name='changepass'),
]

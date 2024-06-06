from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddPostView.as_view(), name='post'),
    path('edit/<int:pk>', views.EditPostView.as_view(), name='edit'),
    path('delete/<int:pk>', views.DeletePostView.as_view(), name='delete'),
]
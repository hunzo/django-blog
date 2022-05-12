from math import frexp

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Publish.as_view(), name='publish'),
    path('editor/', views.Home.as_view(), name='home'),
    path('preview/<int:pk>', views.Preview.as_view(), name='preview'),
    path('add/', views.AddPost.as_view(), name='addPost'),
    path('update/<int:pk>', views.UpdatePost.as_view(), name='updatePost'),
    path('delete/<int:pk>/remove', views.DeletePost.as_view(), name='deletePost'),
]

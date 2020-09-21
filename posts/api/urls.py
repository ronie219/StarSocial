from django.urls import path
from .views import PostListApiView

app_name = 'posts'

urlpatterns = [
    path('',PostListApiView,name ="get"),
]

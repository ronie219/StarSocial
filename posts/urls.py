from django.urls import path,include
from .views import PostList,CreatePost,UserPost,DeletePost,PostDetail

app_name = 'posts'

urlpatterns = [
    path('',PostList.as_view(),name = 'all'),
    path('new/',CreatePost.as_view(),name = 'create'),
    path('by/<username>/<int:pk>/',PostDetail.as_view(),name = 'single'),
    path('delete/<int:pk>/',DeletePost.as_view(),name = 'delete'),
    path('by/<username>/',UserPost.as_view(),name = 'for_user'),
    path('api/post/',include('posts.api.urls','post_api')),
]

from django.urls import path
from .views import Creategroup,SingleGroup,ListGroup,JoinGroup,LeaveGroup

app_name = 'groups'

urlpatterns = [
    path('',ListGroup.as_view(),name = 'all'),
    path('new/',Creategroup.as_view(),name = 'create'),
    path('post/in/<slug>/',SingleGroup.as_view(),name = 'single'),
    path("join/<slug>/",JoinGroup.as_view(),name="join"),
    path("leave/<slug>/",LeaveGroup.as_view(),name="leave"),
]
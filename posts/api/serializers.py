from rest_framework import serializers
from posts.models import Post

class PostListApi(serializers.Serializer):
    class Meta:
        model = Post
        fields = ['user','create_at','message','group']
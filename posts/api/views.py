from posts.models import Post
from .serializers import PostListApi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

@api_view(['GET',])
def PostListApiView(request):
    if request.method == 'GET':
        query = Post.objects.all()
        serial = PostListApi(query)
        return JsonResponse(serial.data)
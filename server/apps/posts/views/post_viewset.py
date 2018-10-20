from rest_framework import viewsets
from rest_framework.response import Response
from apps.posts.serializers import PostSerializer
from apps.posts.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        serialzer = self.serializer_class(self.queryset, many=True)
        return Response(serialzer.data)

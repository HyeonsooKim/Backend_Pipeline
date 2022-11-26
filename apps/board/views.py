from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Board
from .serializers import BoardSerializer
from .permissions import IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly


class BoardView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # 현재 요청한 유저를 작성자로 설정
        serializer.save(user=self.request.user)


class BoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.hit += 1  # 조회수 1 증가
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
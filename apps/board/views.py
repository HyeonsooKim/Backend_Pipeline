from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Board
from .serializers import BoardSerializer
from .permissions import IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly
import logging

logger = logging.getLogger('log_file2')

class BoardView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # 현재 요청한 유저를 작성자로 설정
        serializer.save(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print("List")
        logger.info("GET access Board List", extra={'request':request})
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info("POST access Board Creation", extra={'request':request})
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.hit += 1  # 조회수 1 증가
        instance.save()
        serializer = self.get_serializer(instance)
        logger.info("GET access Board Detail", extra={'request':request})
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        logger.info("PUT access Board Detail", extra={'request':request})
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logger.info("DELETE access Board Detail", extra={'request':request})
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
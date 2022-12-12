from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

import json
# Create your views here.
class JsonDataView(APIView):
    """
    로그데이터를 출력합니다.
    """
    def get(self, request):
        with open('./logs/json_logger.log', 'rb') as f:
            log_data = f.read().decode('utf8').split('\n')[:-1]
            data_list = []
            for i in range(-10001, 0, 1):
                if log_data[-1*i] != "":
                    data_list.append(json.loads(log_data[i]))

        return Response(data_list, status=status.HTTP_200_OK)
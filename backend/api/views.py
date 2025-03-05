from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

class KemaPayments(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django!"})
    def post(self, request):
        logger.info(request.data)
        return Response({"message": "Hello from POST Django!"})

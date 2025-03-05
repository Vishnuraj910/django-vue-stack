from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
import logging
import random
import string
logger = logging.getLogger(__name__)
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
char_set = string.ascii_uppercase + string.digits

class KemaPayments(APIView):
    def post(self, request):
        try:   
            payload = request.data
            logger.debug(f"Payload: {payload}")
            data = {
                'order_id': payload.get('order_id', ''.join(random.sample(char_set*6, 6))),
                'customer_id': payload.get('customer_id', 1), 
                'order_date': datetime.datetime.now(), 
                'merchant_uuid': payload.get('merchant_uuid', 'HASHED_MERCHAT_ID_0001'),  
                'amount': payload.get('amount', 0),
                'payment_status_id':  payload.get('payment_status_id', 1), 
                'transaction_id':  payload.get('transaction_id', ''.join(random.sample(char_set*6, 6))), 
                'device_metadata': payload.get('device_metadata', '{}'),
                'currency_id':  payload.get('currency_id', 1), 
            }

            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error in OrderView.post: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
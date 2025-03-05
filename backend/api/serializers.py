from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'customer_id', 'order_date', 'merchant_uuid', 'amount', 'payment_status_id', 'transaction_id', 'device_metadata', 'currency_id']
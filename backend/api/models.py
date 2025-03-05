from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)  
    customer_id = models.IntegerField()  
    order_date = models.DateTimeField(auto_now_add=True)  
    merchant_uuid = models.CharField(255)  
    amount = models.IntegerField()  
    payment_status_id = models.IntegerField()  
    transaction_id = models.CharField(max_length=50) 
    device_metadata = models.CharField(max_length=255) 
    currency_id = models.IntegerField()
    class Meta:
        db_table = 'orders'
    def __str__(self):
        return f"Order {self.order_id}"
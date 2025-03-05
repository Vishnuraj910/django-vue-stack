from django.db import models

# Create your models here.
class Orders(models.Model):  
    order_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField() 
    order_date = models.DateTimeField( auto_now_add=True)         
    merchant_id = models.IntegerField()
    amount = models.IntegerField()  
    payment_status = models.IntegerField()  
    transaction_id = models.CharField(max_length=50)
    device_metadata = models.CharField(max_length=255)
    currency = models.IntegerField()
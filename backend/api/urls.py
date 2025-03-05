from django.urls import path
from .views import KemaPayments

urlpatterns = [
    path('process/', KemaPayments.as_view(), name='process'),
]
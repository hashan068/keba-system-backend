from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Customer, Product, RFQ, RFQItem, SalesOrder, SalesOrderItem, Quotation, QuotationItem
from .serializers import CustomerSerializer, ProductSerializer,RFQSerializer, RFQItemSerializer, SalesOrderSerializer, SalesOrderItemSerializer, QuotationSerializer, QuotationItemSerializer
import requests
from django.http import JsonResponse
from django.conf import settings

def send_simple_message(to_email, subject, text):
    return requests.post(
        f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages",
        auth=("api", settings.MAILGUN_API_KEY),
        data={
            "from": f"Excited User <mailgun@{settings.MAILGUN_DOMAIN}>",
            "to": [to_email],
            "subject": subject,
            "text": text,
        }
    )

def send_quotation_email(request, quotation_id):
    try:
        # Fetch the quotation details (assuming you have a model named Quotation)
        quotation = Quotation.objects.get(id=quotation_id)
        to_email = quotation.customer.email
        subject = f"Quotation #{quotation.quotation_number}"
        text = f"Dear {quotation.customer.name},\n\nPlease find your quotation details below:\n\nQuotation Number: {quotation.quotation_number}\nTotal Amount: {quotation.total_amount}\n\nThank you!"
        
        response = send_simple_message(to_email, subject, text)
        
        if response.status_code == 200:
            return JsonResponse({'message': 'Email sent successfully!'}, status=200)
        else:
            return JsonResponse({'error': 'Error sending email'}, status=500)
    except Quotation.DoesNotExist:
        return JsonResponse({'error': 'Quotation not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RFQItemViewSet(viewsets.ModelViewSet):
    queryset = RFQItem.objects.all()
    serializer_class = RFQItemSerializer

class RFQViewSet(viewsets.ModelViewSet):
    queryset = RFQ.objects.all()
    serializer_class = RFQSerializer

class QuotationItemViewSet(viewsets.ModelViewSet):
    queryset = QuotationItem.objects.all()
    serializer_class = QuotationItemSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            quotation = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesOrderItemViewSet(viewsets.ModelViewSet):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

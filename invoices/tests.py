# invoices/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-02-22', customer_name='John Doe')

    def test_create_invoice(self):
        data = {
            'date': '2024-02-23',
            'customer_name': 'Jane Doe',
        }
        response = self.client.post('/api/invoices/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)


class InvoiceDetailAPITestCase(APITestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-02-22', customer_name='John Doe')
        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.invoice,
            description='Item 1',
            quantity=2,
            unit_price=10.5,
            price=21.0
        )

    def test_create_invoice_detail(self):
        data = {
            'invoice': self.invoice.id,
            'description': 'Item 2',
            'quantity': 3,
            'unit_price': 15.75,
            'price': 47.25,
        }
        response = self.client.post('/api/invoice-details/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 2)



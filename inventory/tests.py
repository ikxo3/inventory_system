from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product, Supplier, Customer, Invoice

class AuthenticationTests(APITestCase):
    def test_register_user(self):#test for new user
        data = {"username": "testuser", "email": "test@mail.com", "password": "testpass123"}
        response = self.client.post("/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):#test for token
        user = User.objects.create_user(username="testuser", email="test@mail.com", password="testpass123")
        data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post("/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


class ProductTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@mail.com", password="testpass123")
        self.client.force_authenticate(user=self.user)  #for login
#creation of product
        self.product = Product.objects.create(name="Laptop", price=1000.00, quantity=10)

    def test_get_products(self):
        #products list
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
    
        data = {"name": "Smartphone", "price": 500.00, "quantity": 5}
        response = self.client.post("/products/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
    #test of PUT method
        data = {"name": "Updated Laptop", "price": 1200.00, "quantity": 8}
        response = self.client.put(f"/products/{self.product.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        #DELEAT
        response = self.client.delete(f"/products/{self.product.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_product_permissions(self):
        #test if the user can access the product after logging out
        self.client.logout()
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



#filter test

    def test_filter_products(self):
        response = self.client.get("/products/?price=1000.00")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_search_products(self):
        response = self.client.get("/products/?search=Laptop")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)







#404
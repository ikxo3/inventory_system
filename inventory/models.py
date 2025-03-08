from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
  
    def __str__(self):  
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)  
    date = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Canceled', 'Canceled')],
        default='Pending'
    )

    @property
    def total_price(self):
        return sum(product.price for product in self.products.all())

    def __str__(self):
        return f'Invoice #{self.id} - {self.customer.name}'

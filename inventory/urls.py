from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet, CustomerViewSet, InvoiceViewSet ,AuthViewSet



router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'customers', CustomerViewSet)



router.register(r'invoices', InvoiceViewSet)
router.register(r'auth', AuthViewSet, basename="auth")
urlpatterns = [
    path('', include(router.urls)),
    
]

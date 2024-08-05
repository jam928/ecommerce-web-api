print("Loading product_urls.py")
from django.urls import path
from base.views import product_views as views
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('', views.getProducts, name="products"),
    path('<str:pk>', views.getProduct, name="product")
]
from django.urls import path
from . import views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name="products"),
    path('users/profile/', views.getUserProfile, name="users-profile"),
    path('users/', views.getUsers, name="users"),
    path('product/<str:pk>', views.getProduct, name="product")
]
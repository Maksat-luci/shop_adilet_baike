from django.urls import path

from product.models import Product
from product.views import HomePageView, productDetailsView, ProductsListView

# from views import homepage as
urlpatterns = [
    path('', HomePageView.as_view(),name='index-page'),
    path('products/<slug:category_slug>/', ProductsListView.as_view(),name='products-list'),
    path('products/details/<int:pk>/',productDetailsView.as_view(),name="product-details"),
]



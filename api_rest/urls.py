from django.urls import path
from . import views
urlpatterns = [
    path('', views.end_points, name="endpoints"),
    path('get_products', views.get_products, name="products"),
    path('get_categories', views.get_categories, name="categories"),
]
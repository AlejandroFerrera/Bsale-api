from django.http import JsonResponse
from .models import Category, Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializaer, ProductSerializer


api_view(['GET'])
def end_points(request):
    if request.method == "GET":
        return JsonResponse({
            'GET /get_categories': 'Get all categories',
            'GET /get_products': 'Get all products'
        })

@api_view(['GET'])
def get_products(request):
    if request.method == 'GET':
        category = request.GET.get('category') if request.GET.get('category') != None else ""
        products = Product.objects.filter(category__name__icontains=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializaer(categories, many=True)
        return Response(serializer.data)
    

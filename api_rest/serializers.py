from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    url_image =serializers.CharField(max_length=200)
    price = serializers.FloatField()
    discount = serializers.IntegerField()
    category_id = serializers.IntegerField()

class CategorySerializaer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length = 200)
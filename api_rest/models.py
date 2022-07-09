from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=255)
    url_image = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.IntegerField()
    category = models.ForeignKey(Category,on_delete= models.CASCADE, db_column='category')

    class Meta:
        managed = False
        db_table = 'product'

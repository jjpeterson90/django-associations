from django.db import models





class User(models.Model):
    # reviewed_products
    # shop
    pass


class Shop(models.Model):
    # owner
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shop")
    # products
    pass


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products")
    # reviews
    pass


class Review(models.Model):
    # product
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    # user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewed_products")
    pass
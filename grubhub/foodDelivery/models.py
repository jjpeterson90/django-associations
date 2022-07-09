from django.db import models

# Create your models here.
class User(models.Model):
    # orders
    
    # food_items
    pass


class Restaurant(models.Model):
    # orders
    pass


class FoodItem(models.Model):
    
    pass


class Order(models.Model):
    # user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    # restaurant
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders")
    # order_food_items
    food_items = models.ManyToManyField(FoodItem, through="OrderFoodItem", related_name="orders")
    pass


class OrderFoodItem(models.Model):
    # order
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # food_item
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    pass

    class Meta:
        unique_together = (("order", "food_item"))


# Order = user, restaurant
# OrderFoodItem = order, food_item

# user.orders

# order.user
# order.restaurant

# restaurant.orders

# fooditem.orders

# order.food_items

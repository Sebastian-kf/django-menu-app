from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Define choices outside the model
class ItemType(models.IntegerChoices):
    HOT_BEVERAGE = 1, 'Hot Beverage'
    COLD_BEVERAGE = 2, 'Cold Beverage'
    STARTER = 3, 'Starter'
    MAIN_MEAL = 4, 'Main Meal'
    DESSERT = 5, 'Dessert'
    SIDES = 6, 'Sides'

class MenuItem(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    menu_item_name = models.CharField(max_length=200, null=False)
    item_price = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999999)], null=False
    )
    item_in_stock = models.BooleanField(null=False)
    item_description = models.TextField(max_length=1000)
    item_type = models.IntegerField(choices=ItemType.choices, default=ItemType.STARTER)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.menu_item_name

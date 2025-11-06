from django.db import models
from django.db.models import TextChoices
from django.core.validators import MaxValueValidator, MinValueValidator


class ColorChoices(TextChoices):
    BALCK = ['black', 'Black']
    WHITE = ['white', 'White']
    RED = ['red', 'Red']
    BLUE = ['blue', 'Blue']
    GREEN = ['green', 'Green']
    YELLOW = ['yellow', 'yellow']
    ORANGE = ['orange', 'Orange']
    PURPLE =  ['purlple', 'Purple']
    PINK = ['pink', 'Pink']
    GRAY = ['gray', 'Gray']


class DeliveryTimeChoices(TextChoices):
    ONE_DAY = ('1_day', '1 Day Delivery')
    TWO_DAYS = ('2_days', '2 Days Delivery')
    THREE_FOUR_DAYS = ('3_4_days', '3–4 Days Delivery')
    FIVE_SEVEN_DAYS = ('5_7_days', '5–7 Days Delivery')
    TEN_FOURTEEN_DAYS = ('10_14_days', '10–14 Days Delivery')
    TWO_THREE_WEEKS = ('2_3_weeks', '2–3 Weeks Delivery')
    THREE_FOUR_WEEKS = ('3_4_weeks', '3–4 Weeks Delivery')
    ONE_MONTH = ('1_month', '1 Month Delivery')
    TWO_MONTHS = ('2_months', '2 Months Delivery')


class SizeChoices(TextChoices):
    XS = ('xs', 'Extra Small')
    S = ('s', 'Small')
    M = ('m', 'Medium')
    L = ('L', 'Large')
    XL = ('xl', 'Extra Large')
    XXL = ('xxl', '2x Large')
    ONE_SIZE = ('one_size', 'One Size')
    CUSTOM = ('Custom', 'Custom Size')



class Category(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    decs = models.TextField()
    image = models.FileField(upload_to='image/category')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/sub-category')
    color = models.CharField(max_length=50, choices=ColorChoices.choices, default=ColorChoices.GREEN)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategory')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    main_image = models.FileField(upload_to='image/product')
    color = models.CharField(max_length=100, choices=ColorChoices.choices, default=ColorChoices.WHITE)
    quantity = models.PositiveIntegerField(default=1)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='products')
    guarantee = models.PositiveSmallIntegerField(default=1)
    delivery_time = models.CharField(max_length=50, choices=DeliveryTimeChoices.choices, default=DeliveryTimeChoices.TWO_DAYS)
    review = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=100, choices=SizeChoices.choices, blank=True, null=True)
    discount = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    rate = models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10)])
    recomended = models.BooleanField(default=False)
    company = models.CharField(max_length=100)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE, related_name='products')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='image/product')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='image')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Country(models.Model):
    name = models.CharField(max_length=70)
    icon = models.FileField(upload_to='image/flag')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Services(models.Model):
    image = models.FileField(upload_to='image/sevices')
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=190)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
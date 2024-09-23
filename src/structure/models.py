from django.core.validators import MinValueValidator
from django.db import models
from django.utils.timezone import now

from src.base.models import BaseModel
from src.users.models import CustomUser


class Category(BaseModel):
    """
    category model
    """
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    """
    product model
    """

    class PriceType(models.IntegerChoices):
        USZ = 1
        RUB = 2
        USD = 3
        EUR = 4

    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    desc = models.TextField(max_length=1500)
    country = models.CharField(max_length=256)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.CharField(max_length=9, blank=True)
    price = models.FloatField(default=0, validators=[MinValueValidator(0)])
    price_type = models.PositiveSmallIntegerField(choices=PriceType.choices)
    comforts = models.ManyToManyField('Comfort', blank=True)
    max_humans = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class ProductRule(BaseModel):
    """
    product qoidalari yani uy ijaraga olayotgandagi qoidalar
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    """
    product image model
    """
    img = models.ImageField(upload_to='media/product/%Y/%m/%d/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductLike(BaseModel):
    """
    product like model
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)


class Comfort(BaseModel):
    """
    product comfort model qulayliklar
    """
    icon = models.ImageField(upload_to='media/products/icons/%Y/%m/%d/')
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)

    def __str__(self):
        return self.title


class Rent(BaseModel):
    class StatusType(models.IntegerChoices):
        Want_to_get = 1
        Confirmed = 2
        Canceled = 3
        Finished = 4

    renter = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    from_date = models.DateTimeField(validators=[MinValueValidator(now().today)])
    to_date = models.DateTimeField(validators=[MinValueValidator(now().today)])

    adult = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    child = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    baby = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    pet = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    status = models.PositiveSmallIntegerField(choices=StatusType.choices)

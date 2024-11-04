from django.db import models


class ProductStatus(models.TextChoices):
    active = 'active', 'Active'
    deleted = 'deleted', 'Deleted'
    not_available = 'not_available', 'Not Available'


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    status = models.CharField(choices=ProductStatus.choices, max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

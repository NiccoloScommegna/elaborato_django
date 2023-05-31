from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="uploads/product_images/", blank=True, null=True)

    def __str__(self):
        return self.name

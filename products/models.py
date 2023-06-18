from django.db import models

from categories.models import Category

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)#
    stock = models.IntegerField()
    categoria = models.ForeignKey(Category,null=True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

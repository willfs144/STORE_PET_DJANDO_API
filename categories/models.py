from django.db import models


class Category(models.Model):    
    title = models.CharField(max_length=50)
    description = models.TextField()
    #products = models.ManyToManyField(Product, blank=True)
    #products = models.ForeignKey(Product, blank=True,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


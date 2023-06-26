from django.db import models



class Category(models.Model):    
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=200)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    #products = models.ManyToManyField(Product, blank=True)
    #products = models.ForeignKey(Product, blank=True,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


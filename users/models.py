from django.db import models

from django.contrib.auth.models import User

#Model hereda de otro modelo 
class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)



from django.db import models

# Create your models here.
class ContactsUser(models.Model):
    fullName = models.CharField(max_length=100)
    numberPhone = models.CharField(max_length=15,unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.fullName}-{self.numberPhone}"
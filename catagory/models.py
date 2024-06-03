from django.db import models

# Create your models here.
class Catagory(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.name}'
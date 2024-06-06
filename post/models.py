from django.db import models
from catagory.models import Catagory
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField() 
    catagory = models.ManyToManyField(Catagory)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/media/uploads/',blank=True,null=True)
    published_date = models.DateField(default=datetime.datetime.now())
    def __str__(self):
        return f'{self.title}, auth: {self.author}'
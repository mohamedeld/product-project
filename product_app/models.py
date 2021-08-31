from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=100)
    pub_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    body = models.TextField(blank=True)
    url = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    votes_total = models.IntegerField(blank=True, null=True,default=1)

    def __str__(self):
        return self.title

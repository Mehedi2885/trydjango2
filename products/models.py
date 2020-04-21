from django.db import models


# Create your models here.
from django.urls import reverse


class Products(models.Model):
    title = models.CharField(max_length=200)  # max_length required
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    summery = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)
    test = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("products:search-detail", kwargs={"id": self.id})  #f"/search/{self.id}"

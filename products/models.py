from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)  # max_length required
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    summery = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)
    test = models.TextField(blank=True)

    def get_absolute_url(self):
        return f"/search/{self.id}"

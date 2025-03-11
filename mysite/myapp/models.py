from django.db import models


class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField(blank=False, null=True)
  description = models.CharField(max_length=400, blank=False, null=True)
  image = models.ImageField(blank=True, upload_to="images")

  def __str__(self):
    return self.name

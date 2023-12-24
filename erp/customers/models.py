from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name


# Create your models here.

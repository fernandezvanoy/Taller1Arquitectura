from django.db import models
from django.conf import settings
from negocios.models import Product

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PositiveReview(Review):
    pass

class NeutralReview(Review):
    pass

class NegativeReview(Review):
    pass

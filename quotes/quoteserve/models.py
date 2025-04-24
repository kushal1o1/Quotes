from django.db import models

# Create your models here.

class PreQuote(models.Model):
    quote_text = models.TextField()  # Quote text
    author = models.CharField(max_length=255)  # Author name
    categories = models.CharField(max_length=500)  # Categories/tags

    def __str__(self):
        return f"{self.quote_text[:50]}... - {self.author}"

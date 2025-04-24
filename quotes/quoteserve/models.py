from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PreQuote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)  # User who created the quote
    quote_text = models.TextField()  # Quote text
    author = models.CharField(max_length=255)  # Author name
    categories = models.CharField(max_length=500)  # Categories/tags
    posted_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # Date when the quote was created

    def __str__(self):
        return f"{self.quote_text[:50]}... - {self.author}"

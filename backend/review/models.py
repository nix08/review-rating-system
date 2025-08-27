from django.db import models

# Create your models here.

class Review(models.Model):
    name=models.CharField(max_length=25)
    review=models.TextField()
    rating=models.IntegerField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.review}"

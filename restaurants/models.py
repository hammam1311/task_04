from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField(auto_now=False, auto_now_add=False )
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
# Create your models here.

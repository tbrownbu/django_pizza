from django.db import models
from email.mime import image

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img', blank=True,null=True)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()

    def __str__(self):
        return f"{self.topping_name[:50]}..."

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_text[:50]}..."
from django.contrib import admin
#from xml.entree.ElementTree import Comment

# Register your models here.
from .models import Pizza,Topping,Comment
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)

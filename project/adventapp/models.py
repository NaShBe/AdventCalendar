from django.db import models

class AdventSlot(models.Model):
    date = models.DateField(auto_now_add = False)
    text = models.CharField(max_length = 100)
    image = models.ImageField()
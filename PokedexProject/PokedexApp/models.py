from django.db import models

# Create your models here.

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default='')
    height = models.IntegerField()
    weight = models.IntegerField()
    is_default = models.BooleanField(default=True)
    sprite_url = models.URLField(default='')

    def __str__(self):
        return self.name
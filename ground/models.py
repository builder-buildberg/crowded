from django.db import models

# Create your models here.
# create a model for playing ground for bookings and a solt model
# for the slots in the ground

class Ground(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    owner_contact = models.CharField(max_length=100)
    owner_whatsapp = models.CharField(max_length=100)
    price = models.IntegerField()
    area = models.IntegerField()
    image = models.ImageField(upload_to='gallery')
    has_lights = models.BooleanField(default=False)
    has_drinks = models.BooleanField(default=False)
    has_sport_equipment = models.BooleanField(default=False)
    class Meta:
        ordering = ["-name"]
    
    def __str__(self):
        return self.name
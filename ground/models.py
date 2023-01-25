from django.db import models

# Create your models here.
# create a model for playing ground for bookings and a solt model
# for the slots in the ground

class Ground(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField() 
    num_of_courts = models.IntegerField(default=1)
    sports_type = models.CharField(max_length=100)
    owner_contact = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='gallery')
    has_lights = models.BooleanField(default=False)
    has_drinks = models.BooleanField(default=False)
    map_link = models.CharField(max_length=100)
    class Meta:
        ordering = ["-name"]
    
    def __str__(self):
        return self.name
    
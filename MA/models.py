from django.db import models

# Create your models here.

class ContactModel(models.Model):
    
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    contact = models.PositiveIntegerField()
    email = models.EmailField()
    requirement = models.TextField()
    
class DisplayLocation(models.Model):
    
    location_name = models.CharField(max_length=100)
    text_desc = models.CharField(max_length=100)
    image_display = models.ImageField(upload_to = 'Display_Images/')
    
    def __str__(self):
        return self.location_name

class BunglowModel(models.Model):
    
    bunglow_name = models.CharField(max_length = 100)
    room_size = models.CharField(max_length = 100)
    amenites = models.CharField(max_length = 100)
    images = models.FileField(upload_to = 'Bunglow_Images/')
    location = models.ForeignKey(DisplayLocation,on_delete = models.CASCADE)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    check_in = models.CharField(max_length = 50)
    check_out = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    
    
    def __str__(self):
        return self.bunglow_name

    
class Resort(models.Model):
    
    resort_name = models.CharField(max_length = 100)
    r_image = models.ImageField(upload_to = 'resort_images/')

    

    
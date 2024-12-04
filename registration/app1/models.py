from django.db import models
from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.breed
    

    #new code:


    from django.db import models

class PetAdd(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    #pet_breed_code:
    breed = models.CharField(max_length=100,default='unknown')
    age = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='pet_images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)


def image(self):
        if self.image_upload:
            return self.image_upload.url
        elif self.image_url:
            return self.image_url
        else:
            return None

def save(self, *args, **kwargs):
        if self.image_url:
            # If image URL is provided, clear the uploaded image
            self.image = None
        super().save(*args, **kwargs)

       
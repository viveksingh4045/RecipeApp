from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Create your models here.

User = get_user_model()

class Profile(models.Model):
    '''
    Data Model to create and store User profile information
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    last_updated = models.DateField(default = datetime.now())

    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    '''
    Data model to store recipes informations
    '''
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipename = models.TextField(blank=False, max_length=100)
    recipeimg = models.ImageField(upload_to='recipe_images',default='no_recipe_img.png')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default = datetime.now())
    rating = models.FloatField(default = 0)

    def __str__(self):
        return self.recipename
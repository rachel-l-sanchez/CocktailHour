# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    User
)
import base64
from django.db.models.signals import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


    
class Cocktail(models.Model):
    image = models.ImageField(null=True, default=None, blank=True)
    cocktail_id = models.IntegerField(editable=False, unique = False, default = 1)
    drinkName = models.CharField(max_length = 200, default = "")
    instructions = models.TextField()
    ingredient1 = models.CharField(max_length = 200, default = "")
    ingredient2 = models.CharField(max_length = 200, default = "")
    ingredient3 = models.CharField(max_length = 200, default = "")
    category = models.CharField(max_length = 200, default = "")
    glass = models.CharField(max_length = 200, default = "")
    ingredient4 = models.CharField(max_length = 200, default = "", null = True)
    ingredient5  = models.CharField(max_length = 200, default = "", null = True)
    ingredient6 = models.CharField(max_length = 200, default = "", null = True)
    ingredient7 = models.CharField(max_length = 200, default = "", null = True)
    ingredient8  = models.CharField(max_length = 200, default = "", null = True)
    ingredient9  = models.CharField(max_length = 200, default = "", null = True)
    ingredient10  = models.CharField(max_length = 200, default = "None", null= True)
    ingredient11 = models.CharField(max_length = 200, null = True, default = "None")
    ingredient12  = models.CharField(max_length = 200, default = "None", null = True)
    ingredient13 = models.CharField(max_length = 200, default = "None", null = True)
    ingredient14 = models.CharField(max_length = 200, default = "None", null = True)
    ingredient15  = models.CharField(max_length = 200, default = "None", null = True)
    measure1  = models.CharField(max_length = 200, default = "None", null = True)
    measure2  = models.CharField(max_length = 200, default = "None", null = True)
    measure3  = models.CharField(max_length = 200, default = "None", null = True)
    measure4 = models.CharField(max_length = 200, default = "None", null = True)
    measure5 = models.CharField(max_length = 200, default = "None", null = True)
    measure6 = models.CharField(max_length = 200, default = "None", null = True)
    measure7 = models.CharField(max_length = 200, default = "None", null = True)
    measure8 = models.CharField(max_length = 200, default = "None", null = True)
    measure9 = models.CharField(max_length = 200, default = "None", null = True)
    measure10= models.CharField(max_length = 200, default = "None", null = True)
    measure11= models.CharField(max_length = 200, default = "None", null = True)
    measure12= models.CharField(max_length = 200, default = "None", null = True)
    measure13= models.CharField(max_length = 200, default = "None", null = True)
    measure14= models.CharField(max_length = 200, default = "None", null = True)
    measure15= models.CharField(max_length = 200, default = "None", null = True)
    alcoholic= models.CharField(max_length = 200, default = "None", null = True)

    class Meta:
        app_label = 'cocktail'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_cocktail()                                 # calling the set_uid function

    def set_cocktail(self):
        if not self.cocktail_id:                               # if uid of the instance is blank
            cocktail_id =str(self.cocktail_id)       # generating the uid
            cocktail= Cocktail.objects.get(cocktail_id=self.cocktail_id)     # getting the instance
            cocktail.cocktail_id = cocktail_id                         # allocating the value
            cocktail.save()                              # saving the instance

    def __str__(self):
        return self.cocktail_id

# class User(models.Model):
#     favorites = models.ManyToManyField(Cocktail, related_name='favorited_by', null=True, blank=True)

#     def __str__(self):
#         return self.user.username

# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete = models.CASCADE)

#     def __str__(self):  
#           return "%s's profile" % self.user 
    
#     def create_user_profile(sender, instance, created, **kwargs):  
#         if created:  
#             profile, created = UserProfile.objects.get_or_create(user=instance)  

#     post_save.connect(create_user_profile, sender=User) 

#     def __str__(self):
#         return self.user.username

    

class CocktailBookmark(models.Model):
    recipe = models.ForeignKey(Cocktail, on_delete = models.PROTECT, related_name = "bookmarks")
    bookmarked_by = models.ForeignKey(User, on_delete =  models.PROTECT)
    bookmarked_at = models.DateTimeField(auto_now_add = True)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_profile')
    favorites = models.ManyToManyField(Cocktail, related_name='favorites', null=True, blank=True)
    bookmarked_at = models.DateTimeField(auto_now_add = True)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.UserProfile.save()


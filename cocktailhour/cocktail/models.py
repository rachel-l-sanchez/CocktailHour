# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    User
)


class Cocktail(models.Model):
    image = models.CharField(max_length = 200 )
    cocktail_uid = models.CharField(null = False, blank = False, max_length = 200, default = "None")
    id = models.AutoField(primary_key=True, editable=False)
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
        if not self.cocktail_uid:                               # if uid of the instance is blank
            cocktail_uid =str(self.cocktail_uid)       # generating the uid
            cocktail= Cocktail.objects.get(cocktail_uid=self.cocktail_uid)     # getting the instance
            cocktail.cocktail_uid = cocktail_uid                         # allocating the value
            cocktail.save()                              # saving the instance

    def __str__(self):
        return self.cocktail_uid



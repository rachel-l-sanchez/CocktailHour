# Cocktail Hour

## Overview
A cocktail recipe application using the cocktail API. Users can log in to their accounts and save their favorite recipes to experiment on their own

## Features
1. Create new cocktail recipes
2. Login/Registration
3. Update Recipe
4. Delete a recipe saved to your account
5. View all recipes
6. View one full recipe

## Code Sample
```
def get_cocktails(request):
    allCocktails = {}
    # res = requests.get(f"https://www.thecocktaildb.com/api/json/v1/{ API_KEY }/search.php?s=margarita")
    url = f"https://www.thecocktaildb.com/api/json/v1/{ API_KEY }/search.php?s=margarita"
    r = requests.get(url)
    tt = json.loads(r.text)
  

    for i in (tt['drinks']):
        print(i, '/n')
        image = i['strDrinkThumb']
        glass = i['strGlass']
        alcoholic = i['strAlcoholic']
        instructions = i['strInstructions']
        ingredient1 = i['strIngredient1']
        ingredient2 = i['strIngredient2']
        ingredient3 = i['strIngredient3']
        drinkName= i['strDrink']
        ingredient4 = i['strIngredient4']
        ingredient5 = i['strIngredient5']
        ingredient6 = i['strIngredient6']
        ingredient7 = i['strIngredient7']
        ingredient8 = i['strIngredient8']
        ingredient9 = i['strIngredient9']
        ingredient10 = i['strIngredient10']
        ingredient11= i['strIngredient11']
        ingredient12= i['strIngredient12']
        ingredient13= i['strIngredient13']
        ingredient14 = i['strIngredient14']
        ingredient15= i['strIngredient15']
        measure1= i['strMeasure1']
        measure2= i['strMeasure2']
        measure3= i['strMeasure3']
        measure4= i['strMeasure4']
        measure5= i['strMeasure5']
        measure6= i['strMeasure6']
        measure7= i['strMeasure7']
        measure8= i['strMeasure8']
        measure9= i['strMeasure9']
        measure10= i['strMeasure10']
        measure11= i['strMeasure11']
        measure12= i['strMeasure12']
        measure13= i['strMeasure13']
        measure14= i['strMeasure14']
        measure15= i['strMeasure15']
        category = i['strCategory']
        cocktail_uid = i['idDrink']
        Cocktail.objects.create(image = image,
        instructions = instructions,
        drinkName = drinkName, ingredient1 = ingredient1,
        ingredient2 = ingredient2, ingredient3 = ingredient3, ingredient4= ingredient4, 
        ingredient5 = ingredient5, ingredient6=ingredient6,
        ingredient7 = ingredient7,
        ingredient8=ingredient8,
        ingredient9 = ingredient9, ingredient10 = ingredient10,
        ingredient11=ingredient11,
        ingredient12 = ingredient12, 
        ingredient13= ingredient13,
        ingredient14 = ingredient14,
        ingredient15 = ingredient15,
        measure1= measure1,
        measure2= measure2,
        measure3= measure3,
        measure4= measure4,
        measure5= measure5,
        measure6= measure6,
        measure7= measure7,
        measure8= measure8,
        measure9= measure9,
        measure10=measure10,
        measure11= measure11,
        measure12= measure12,
        measure13= measure13,
        measure14= measure14,
        measure15=measure15,
        category = category,
        glass = glass,
        alcoholic = alcoholic, cocktail_uid = cocktail_uid)
        allCocktails = Cocktail.objects.all()
    return render (request=request, template_name="cocktail.html", context = {'cocktailData': allCocktails, 'image': image})
```

## Running the Project
1. git clone https://github.com/rachel-l-sanchez/CocktailHour.git
2. python3 manage.py runserver

## Collaborators
None

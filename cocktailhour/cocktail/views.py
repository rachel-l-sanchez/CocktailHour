# Create your views here.
import requests
import json
import webbrowser
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import  render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages``
from django.views import View
from .models import Cocktail
from django.shortcuts import  render, redirect
from .forms import UserRegistrationForm, EditForm, CreateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.management.base import BaseCommand
from django.views.generic import TemplateView

API_KEY = 1

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

def cocktails(request):
    allCocktails = Cocktail.objects.all().order_by('pk')
    return render (request=request, template_name="home.html", context = {'allCocktails': allCocktails})

class Command(BaseCommand):
    def handle(self, *args, **options):
        create()
        # clear_data()
        print("completed")

def updateCocktail(request, cocktail):
    instance = Cocktail.objects.get(cocktail=cocktail)
    form = EditForm(request.POST or None,request.FILES or None, instance = instance)
    if request.method == 'POST':
        drinkName = request.POST['drinkName']
        ingredient1 = request.POST['ingredient1']
        ingredient2 = request.POST['ingredient2']
        ingredient3 = request.POST['ingredient3']
        ingredient4 = request.POST['ingredient4']
        instructions = request.POST['instructions']
        Cocktail.objects.update(
            properties=({"pk" :pk}, {"drinkName": drinkName}, {"ingredient1": ingredient1},
            {"ingredient2": ingredient2},{"ingredient3": ingredient3},{"ingredient4": ingredient4},
             {"instructions": instructions}))
        return redirect('cocktails')
    form = EditForm(instance = instance)
    return render(request, 'edit.html', {'cocktail': instance}, {'form': form})

def delete(request, pk):
    cocktailToDelete = Cocktail.objects.get(pk=pk)
    cocktailToDelete.delete()
    return redirect('cocktails')

def register_request(request, **kwargs):
    form = UserRegistrationForm(request.POST)    
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request,user)
        return redirect('cocktails')
    context = {'form': form}
    return render (request=request, template_name="register.html", context={"form":form})

def login_request(request):
    if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("main:homepage")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("cocktails")


def detail(request, pk):
    cocktail = Cocktail.objects.get(cocktail =cocktail)
    print(cocktail)
    return render (
        request,
        'templates/detail.html',
        {'cocktail': cocktail}
    )
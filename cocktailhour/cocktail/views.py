# Create your views here.
import requests
import json
import webbrowser
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import  render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views import View
from .models import Cocktail
from django.shortcuts import  render, redirect
from .forms import UserRegistrationForm, EditForm, CreateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.management.base import BaseCommand
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.http import HttpResponse
from .models import Cocktail, CocktailBookmark, UserProfile, User
import base64
from django.shortcuts import get_object_or_404


def get_cocktails(request):
    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    response = requests.get(f)
    if response.status_code == requests.codes.ok:
        tt = json.loads(response.text)
        print(tt)
        
    else:
        tt = response.text
        print("Error:", response.status_code, tt)
    data = response.json()
    cocktails = data['drinks']
    for i in cocktails:
        print(i, "/n")
        cocktailData = Cocktail(
        image =i["strDrinkThumb"],
        glass = i['strGlass'],
        alcoholic = i['strAlcoholic'],
        instructions = i['strInstructions'],
        ingredient1 = i['strIngredient1'],
        ingredient2 = i['strIngredient2'],
        ingredient3 = i['strIngredient3'],
        drinkName= i['strDrink'],
        ingredient4 = i['strIngredient4'],
        ingredient5 = i['strIngredient5'],
        ingredient6 = i['strIngredient6'],
        ingredient7 = i['strIngredient7'],
        ingredient8 = i['strIngredient8'],
        ingredient9 = i['strIngredient9'],
        ingredient10 = i['strIngredient10'],
        ingredient11= i['strIngredient11'],
        ingredient12= i['strIngredient12'],
        ingredient13= i['strIngredient13'],
        ingredient14 = i['strIngredient14'],
        ingredient15= i['strIngredient15'],
        measure1= i['strMeasure1'],
        measure2= i['strMeasure2'],
        measure3= i['strMeasure3'],
        measure4= i['strMeasure4'],
        measure5= i['strMeasure5'],
        measure6= i['strMeasure6'],
        measure7= i['strMeasure7'],
        measure8= i['strMeasure8'],
        measure9= i['strMeasure9'],
        measure10= i['strMeasure10'],
        measure11= i['strMeasure11'],
        measure12= i['strMeasure12'],
        measure13= i['strMeasure13'],
        measure14= i['strMeasure14'],
        measure15= i['strMeasure15'],
        category = i['strCategory'],
        cocktail_id = i['idDrink'])
        cocktailData.save()

        # Cocktail.objects.create(image = image,
        # instructions = instructions,
        # drinkName = drinkName, ingredient1 = ingredient1,
        # ingredient2 = ingredient2, ingredient3 = ingredient3, ingredient4= ingredient4, 
        # ingredient5 = ingredient5, ingredient6=ingredient6,
        # ingredient7 = ingredient7,
        # ingredient8=ingredient8,
        # ingredient9 = ingredient9, ingredient10 = ingredient10,
        # ingredient11=ingredient11,
        # ingredient12 = ingredient12, 
        # ingredient13= ingredient13,
        # ingredient14 = ingredient14,
        # ingredient15 = ingredient15,
        # measure1= measure1,
        # measure2= measure2,
        # measure3= measure3,
        # measure4= measure4,
        # measure5= measure5,
        # measure6= measure6,
        # measure7= measure7,
        # measure8= measure8,
        # measure9= measure9,
        # measure10=measure10,
        # measure11= measure11,
        # measure12= measure12,
        # measure13= measure13,
        # measure14= measure14,
        # measure15=measure15,
        # category = category,
        # glass = glass,
        # alcoholic = alcoholic, cocktail_id = cocktail_id)
        cocktailData = Cocktail.objects.all().order_by('cocktail_id')
    return render (request=request, template_name="cocktail.html", context = {'cocktailData': cocktailData})

def cocktails(request):
    allCocktails = Cocktail.objects.all().order_by('pk')
    return render(request=request, template_name="home.html", context = {'allCocktails': allCocktails})

def base64_to_image(base64_string):
    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name=uuid4().hex + "." + ext)


def delete(request,id):
    bookmarkToDelete = get_object_or_404(UserProfile, id= id)
    bookmarkToDelete.delete()
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
                    return redirect("cocktails")
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


def detail(request, id):
    instance = get_object_or_404(Cocktail, id = id)
    return render (
        request,
        template_name='detail.html',
        context = {'cocktail': instance}
    )

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Cocktail
    template_name = "search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Cocktail.objects.filter(
            Q(drinkName__icontains=query) | Q(instructions__icontains=query)
        )
        return object_list



def favorite(request, id):
    if request.method == 'POST':
        favorite = Cocktail.objects.get(id=id)
        user = request.user
        user.favorites.add(favorite)
        messages.add_message(request, messages.INFO, 'Cocktail Favorited.')
        return redirect('home')

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
from django.contrib.auth.forms import AuthenticationForm #add this
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
from django.contrib.auth import get_user_model, User
from django.http import HttpResponse
from django.db import transaction
from .forms import *
from django.contrib.auth import login import login_required

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
    bookmarkToDelete = get_object_or_404(Cocktail, id = id)
    bookmarkToDelete.delete()
    return redirect('cocktails')

def register_request(request, **kwargs):
    form = UserCreationForm(request.POST or None)    
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.save()
            login(request,user)
        return redirect('cocktails')
    return render (request=request, template_name="register.html", context={"form":form})

def updateCocktail(request, id):
    instance = Cocktail.objects.get(id=id)
    form = EditForm(request.POST or None,request.FILES or None, instance = instance)
    if request.method == 'POST':
        editForm = form.save(commit = False)
        image = editForm.image
        instructions =editForm.instructions
        drinkName = editForm.drinkName
        ingredient1 = editForm.ingredient1
        ingredient2 = editForm.ingredient2
        ingredient3 =editForm.ingredient3
        ingredient4= editForm.ingredient4
        ingredient5 = editForm.ingredient5
        ingredient6=editForm.ingredient6
        ingredient7 = editForm.ingredient7
        ingredient8=editForm.ingredient8
        ingredient9 = editForm.ingredient9
        ingredient10 = editForm.ingredient10
        ingredient11=editForm.ingredient11
        ingredient12 = editForm.ingredient12
        ingredient13= editForm.ingredient13
        ingredient14 = editForm.ingredient14
        ingredient15 = editForm.ingredient15
        measure1= editForm.measure1
        measure2= editForm.measure2
        measure3= editForm.measure3
        measure4= editForm.measure4
        measure5= editForm.measure5
        measure6= editForm.measure6
        measure7= editForm.measure7
        measure8= editForm.measure8
        measure9= editForm.measure9
        measure10=editForm.measure10
        measure11= editForm.measure11
        measure12= editForm.measure12
        measure13= editForm.measure13
        measure14= editForm.measure14
        measure15=editForm.measure15
        category = editForm.category
        glass = editForm.glass
        alcoholic = editForm.alcoholic
        editForm.save()
        return redirect('cocktails')
    form = EditForm(instance = instance)
    return render(request, 'edit.html', {'form': form})

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

@login_required
@transaction.atomic
def favorite(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance = request.user.user_profile)
        favorite_form = FavoriteForm(request.POST, instance = request.user.favorites)
        if profile_form.is_valid() and favorite_form.is_valid():
            profile_form.save()
            favorite_form.save()
            messages.success(request,_('Your profile was successfully updated'))
            return redirect('detail')
        else:
            messages.error(request,_('Please correct the errors'))
    else:
        profile_form = ProfileForm(instance = request.user.user_profile)
        favorite_form = FavoriteForm(instance = request.user.favorites)
        # cocktail = Cocktail.objects.get(id=cocktail_id)
        # user = get_object_or_404(User, id=request.user.id)
        # user.user_profile.favorites.add(cocktail)
        # user.save()
        # user = request.user
        # user.favorites.create(cocktail)
        # profile = UserProfile.objects.get(id = user_id)
        # UserProfile = get_user_model()
        # user.favorites(cocktail)
    return render(request, 'detail.html', {'profile_form': profile_form, 'favorite_form': favorite_form})
